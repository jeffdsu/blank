from inspiration.models import MediumType, Contributor, Checkout, Insight, Keyword, WordToIgnore, InsightTag, Medium, ContributionType, Tag
from inspiration.serializers import MediumTypeSerializer, ContributorSerializer, CheckoutSerializer, InsightSerializer, InsightWithKeywordsSerializer, MediumSerializer, \
    UserPublicSerializer, KeywordSerializer, WordToIgnoreSerializer, ContributionTypeSerializer, TagSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
import random

from inspiration.views.InpsiprationBaseViewMixIn import InspirationBaseViewMixIn

class ProfileViewSet (viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Insight.objects.all()
    serializer_class = InsightWithKeywordsSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, users_pk=None):
        try:

            return_params_dict = self.read_return_params()

            print(request.user)

            user = request.user

            personal = self.request.query_params.get('personal', None)

            # TODO-JEFF there has to be a better way to do this
            insights = None
            if personal is not None:
                insights = Insight.search(user=user, personal=bool(personal))
            else:
                insights = Insight.search(user=user)

            return self.respond_ok(self.log_msg, self.request, self.serializer(insights, return_params_dict).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)

    def serializer(self, objs, return_params_dict):
        if 'top_10_keywords' in return_params_dict:
            return InsightWithKeywordsSerializer(objs, many=True)
        else:
            return InsightSerializer(objs, many=True)