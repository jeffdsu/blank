from inspiration.models import MediumType, Contributor, Checkout, Insight, Keyword, WordToIgnore, Medium
from inspiration.serializers import MediumTypeSerializer, ContributorSerializer, CheckoutSerializer, InsightSerializer, MediumSerializer, \
    UserSerializer, KeywordSerializer, WordToIgnoreSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random

from inspiration.views.InpsiprationBaseViewMixIn import InspirationBaseViewMixIn


class MediumTypeViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = MediumType.objects.all()
    serializer_class = MediumTypeSerializer


class KeywordsViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Keyword.objects.filter()
    serializer_class = KeywordSerializer

    def list(self, request, media_pk=None):
        medium = Medium.get(media_pk)

        format_qp = self.request.query_params.get('style', None)
        kwargs = dict()
        if format_qp:
            kwargs['style'] = format_qp
        medium_keywords = Keyword.search(medium, **kwargs)
        print(len(medium_keywords))

        # if format_qp is not None:

        return Response(KeywordSerializer(medium_keywords, many=True).data)


class MediumViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Medium.objects.all()
    serializer_class = MediumSerializer

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)


class ContributorViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Contributor.objects.all()
    serializer_class = Contributor


class CheckoutViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class MediumInsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = InsightSerializer

    def list(self, request, media_pk=None):
        try:
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

                query = Q(medium=medium, valid=True)
                keyword_q = Q()

                for keyword in keywords:
                    keyword_q |= Q(lesson__icontains=keyword.word)

                insights = Insight.objects.filter(query & keyword_q)
                for i in insights:
                    print(i.lesson)


                return Response(InsightSerializer(random.choice(insights)).data)

            else:
                insights = Insight.search(medium=medium, valid=True)

                return Response(InsightSerializer(insights, many=True).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)

    def create(self, request, media_pk=None):
        try:
            medium = Medium.get(media_pk)
            user = request.user
            lesson = request.data['lesson']

            temp_insight = Insight(medium=medium, user=user, lesson=lesson, valid=False)

            temp_insight.save()

            return Response(InsightSerializer(temp_insight).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)



class InsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = InsightSerializer
    queryset = Insight.objects.all()

    def list(self, request):

        insights = Insight.objects.all()

        return Response(InsightSerializer(insights, many=True).data)

    def create(self, request, media_pk=None):

        insight_dict = dict()
        insight_dict['user'] = request.user
        insight_dict['lesson'] = request.data['lesson']
        insight_dict['book_id'] = media_pk
        insight_dict['checkout'] = request.data['checkout'] if 'checkout' in request.data else None

        insight = Insight(**insight_dict)
        insight.save()

        return Response(InsightSerializer(insight).data)




class WordsToIgnoreViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = WordToIgnore.objects.all()
    serializer_class = WordToIgnoreSerializer

    def create(self, request):

        try:

            new_word = WordToIgnore.search(word=request.data['word'])

            if new_word:
                return WordToIgnore.respond_already_found(word=request.data['word'])

            new_word = WordToIgnore(word=request.data['word'])
            medium_keywords = Keyword.admin_search(word=request.data['word'])

            medium_keywords.delete()
            new_word.save()

            return Response(WordToIgnoreSerializer(new_word).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)


class UserViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    queryset = User.objects.all()
    serializer = UserSerializer()


class ContributorMediaViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Medium.objects.all()
    serializer_class = ContributorSerializer

    def list(self, request, medium_contributor_pk=None):
        try:
            contributor = Contributor.get(medium_contributor_pk)
            mediums = Medium.search(contributor=contributor)

            return Response(MediumSerializer(mediums, many=True).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)


class UserInsightsViewSet (viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

    def list(self, request, users_pk=None):
        try:
            user = User.objects.get(id=users_pk)
            insights = Insight.search(user=user)

            return Response(InsightSerializer(insights, many=True).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)






