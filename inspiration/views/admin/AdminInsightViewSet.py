from inspiration.models import Book, Insight
from inspiration.serializers import  InsightSerializer
from rest_framework import viewsets, permissions
from inspiration.views import InspirationBaseViewMixIn
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route

class AdminInsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    serializer_class = InsightSerializer
    queryset = Insight.objects.all()

    # TODO - this should be an admin only api
    @detail_route(methods=['put'])
    def validate(self, request, pk=None):
        '''
        Used to validate a specific insight.  This will call the parse lesson function.
        :param request:
        :param books_pk:
        :return:
        '''

        try:
            insight = Insight.get(pk)
            book = Book.get(insight.book.id)

            # if the insight is already set to true, don't do anything
            # should this be a 200 response?
            if insight.valid == True:
                return insight.respond_nothing_done()

            from inspiration.learning.BookLearning import BookLearning

            response = BookLearning.learn(book, insight)

            insight.valid = True
            insight.save()

            return response

        except Exception as exception:
            return self.__class__.respondToException(exception)