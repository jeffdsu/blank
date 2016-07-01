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

class ContributionTypeViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = ContributionType.objects.all()
    serializer_class = ContributionTypeSerializer


class MediumTypeViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = MediumType.objects.all()
    serializer_class = MediumTypeSerializer

class TagViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class KeywordsViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Keyword.objects.filter()
    serializer_class = KeywordSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, type=None, media_pk=None):
        medium = Medium.get(media_pk)

        format_qp = self.request.query_params.get('style', None)
        kwargs = dict()
        if format_qp:
            kwargs['style'] = format_qp
        medium_keywords = Keyword.search(medium, **kwargs)
        print(len(medium_keywords))

        # if format_qp is not None:

        return self.respond_ok(self.log_msg, self.request, KeywordSerializer(medium_keywords, many=True).data)


class MediumViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Medium.objects.all()
    serializer_class = MediumSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, type=None):
        mediums = Medium.objects.filter(type__name=type)

        return self.respond_ok(self.log_msg, self.request, MediumSerializer(mediums, many=True).data)

    @InspirationBaseViewMixIn.blank_logging_decorator
    def retrieve(self, request, type=None, pk=None):

        medium = Medium.get(pk)
        return self.respond_ok(self.log_msg, self.request, MediumSerializer(medium).data)




class ContributorViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class CheckoutViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (AllowAny,)

    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class MediumInsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):

    permission_classes = (AllowAny,)

    serializer_class = InsightSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, type=None, media_pk=None):


        try:

            return_params_dict = self.read_return_params()

            medium = Medium.get(media_pk)

            random_top_10_qp = self.request.query_params.get('random_top_10', None)


            if random_top_10_qp is not None:

                keywords = None
                if self.request.query_params.getlist('keywords_filter'):
                    keywords = []
                    for keyword in self.request.query_params.getlist('keywords_filter'):
                        keywords.append(Keyword(word=keyword))
                else:
                    keywords = Keyword.get_top_10_keywords(medium)

                insight = Insight.random_for_medium(medium, keywords)

                return self.respond_ok(self.log_msg, self.request, self.serializer([insight], return_params_dict).data)

            else:
                insights = Insight.search(medium=medium, valid=True)

                return self.respond_ok(self.log_msg, self.request, self.serializer(insights, return_params_dict).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)


    def serializer (self, objs, return_params_dict):
        if 'top_10_keywords' in return_params_dict:
            return InsightWithKeywordsSerializer(objs, many=True)
        else:
            return InsightSerializer(objs, many=True)

    @authentication_classes(TokenAuthentication,)
    @InspirationBaseViewMixIn.blank_logging_decorator
    def create(self, request,  type=None, media_pk=None):
        try:
            medium = Medium.get(media_pk)
            user = request.user
            tags_data = request.data.pop('tags')


            temp_insight = Insight(medium=medium, user=user, **request.data)
            temp_insight.save(tags_data)

            for tag_data in tags_data:
                tag = Tag.objects.get_or_create(**tag_data)[0]
                InsightTag.objects.get_or_create(insight=temp_insight, tag=tag)

            return self.respond_ok(self.log_msg, self.request, InsightSerializer(temp_insight).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)



class InsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    serializer_class = InsightSerializer
    queryset = Insight.objects.all()

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request):

        insights = Insight.objects.all()

        return self.respond_ok(self.log_msg, self.request, InsightSerializer(insights, many=True).data)

    @InspirationBaseViewMixIn.blank_logging_decorator
    def create(self, request, media_pk=None):

        insight_dict = dict()
        insight_dict['user'] = request.user
        insight_dict['lesson'] = request.data['lesson']

        insight_dict['book_id'] = media_pk
        insight_dict['checkout'] = request.data['checkout'] if 'checkout' in request.data else None

        insight = Insight(**insight_dict)
        insight.save()

        return self.respond_ok(self.log_msg, self.request, InsightSerializer(insight).data)




class WordsToIgnoreViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = WordToIgnore.objects.all()
    serializer_class = WordToIgnoreSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def create(self, request):

        try:

            new_word = WordToIgnore.search(word=request.data['word'])

            if new_word:
                return self.respond(WordToIgnore.respond_already_found(word=request.data['word']))

            new_word = WordToIgnore(word=request.data['word'])
            medium_keywords = Keyword.admin_search(word=request.data['word'])

            medium_keywords.delete()
            new_word.save()

            return self.respond_ok(self.log_msg, self.request, WordToIgnoreSerializer(new_word).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)


class UserViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer


class ContributorWorksViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Medium.objects.all()
    serializer_class = ContributorSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, contributors_pk=None):
        try:
            contributor = Contributor.get(contributors_pk)
            mediums = Medium.search(contributions__contributor=contributor)

            return self.respond_ok(self.log_msg, self.request, MediumSerializer(mediums, many=True).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)



class UserInsightsViewSet (viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, users_pk=None):
        try:
            return_params_dict = self.read_return_params()

            user = User.objects.get(id=users_pk)
            insights = Insight.search(user=user)

            return self.respond_ok(self.log_msg, self.request, self.serializer(insights, return_params_dict).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)

    def serializer(self, objs, return_params_dict):
        if 'top_10_keywords' in return_params_dict:
            return InsightWithKeywordsSerializer(objs, many=True)
        else:
            return InsightSerializer(objs, many=True)




