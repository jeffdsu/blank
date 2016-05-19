from inspiration.models import Medium, Insight
from inspiration.serializers import  InsightSerializer
from rest_framework import viewsets, permissions
from inspiration.views import InspirationBaseViewMixIn
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import detail_route
from inspiration.learning.MediumLearning import MediumLearning

class AdminInsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    serializer_class = InsightSerializer
    queryset = Insight.objects.all()

    # TODO - this should be an admin only api
    @detail_route(methods=['put'])
    def validate(self, request, pk=None):

        try:
            insight = Insight.get(pk)
            medium = Medium.get(insight.medium.id)

            # if the insight is already set to true, don't do anything
            # should this be a 200 response?
            if insight.valid == True:
                return insight.respond_nothing_done()

            response = MediumLearning.learn(medium, insight)

            insight.valid = True
            #insight.save()

            return response

        except Exception as exception:
            return self.__class__.respondToException(exception)