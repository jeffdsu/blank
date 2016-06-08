from inspiration.models import Medium, Insight, WordToIgnore
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
    @InspirationBaseViewMixIn.blank_logging_decorator
    def validate(self, request, pk=None):

        try:

            insight = Insight.get(pk)
            medium = Medium.get(insight.medium.id)
            words_to_ignore_dict = WordToIgnore.get_dict()

            # Blank - if the insight is already set to true, don't do anything
            # Jeff - should this be a 200 response?
            if insight.valid == True:
                return self.__class__.respond_nothing_done(self.log_msg, self.request)

            response = MediumLearning.learn(medium, insight, words_to_ignore_dict, log_msg=self.log_msg)

            insight.valid = True
            insight.save()

            self.__class__.logger.write_log_message(self.log_msg, request, 200)
            return response

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)


