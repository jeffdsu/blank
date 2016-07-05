from inspiration.models import MediumType, Contributor, Checkout, Insight, Keyword, WordToIgnore, InsightTag, Medium, ContributionType, Tag, Note, Moment, MomentType
from inspiration.serializers import MediumTypeSerializer, ContributorSerializer, CheckoutSerializer, InsightSerializer, InsightWithKeywordsSerializer, MediumSerializer, \
    UserPublicSerializer, KeywordSerializer, WordToIgnoreSerializer, ContributionTypeSerializer, TagSerializer, MomentTypeSerializer, MomentSerializer, NoteSerializer
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


class MediumViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Tag.objects.all()
    serializer_class = MediumSerializer

class MomentTypeViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = MomentType.objects.all()
    serializer_class = MomentTypeSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, type=None):

        moment_types = MomentType.objects.filter()

        return self.respond_ok(self.log_msg, self.request, MomentTypeSerializer(moment_types, many=True).data)

    @InspirationBaseViewMixIn.blank_logging_decorator
    def create(self, request):
        try:

            new_moment_type = MomentType(**request.data)

            new_moment_type.save()

            return self.respond_created(self.log_msg, self.request, MomentTypeSerializer(new_moment_type).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)



class NoteViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MomentViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Moment.objects.all()
    serializer_class = MomentSerializer

    @InspirationBaseViewMixIn.blank_logging_decorator
    def list(self, request, type=None):

        user = request.user

        moments = Moment.objects.filter(user=user)

        return self.respond_ok(self.log_msg, self.request, MomentSerializer(moments, many=True).data)


    @InspirationBaseViewMixIn.blank_logging_decorator
    def create(self, request):

        try:

            user = request.user
            insight_data = request.data.pop('insight')
            moment_type_data = request.data.pop('type')
            moment_type = MomentType.get(moment_type_data['id'])

            insight = Insight.get(insight_data['id'])

            new_moment = Moment(user=user, insight=insight, type=moment_type, **request.data)

            new_moment.save()

            return self.respond_created(self.log_msg, self.request, MomentSerializer(new_moment).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)


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
                insights = Insight.search(medium=medium, valid=True, personal=False)

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

            default_valid=False
            if "personal" in request.data and request.data['personal']==True:
                default_valid = True

            temp_insight = Insight(valid=default_valid, medium=medium, user=user, **request.data)
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

        print(request.data)
        tags_data = request.data.pop('tags')

        temp_insight = Insight(user=request.user, **request.data)
        temp_insight.save()

        for tag_data in tags_data:
            tag = Tag.objects.get_or_create(**tag_data)[0]
            InsightTag.objects.get_or_create(insight=temp_insight, tag=tag)

        return self.respond_ok(self.log_msg, self.request, InsightSerializer(temp_insight).data)

    @InspirationBaseViewMixIn.blank_logging_decorator
    def update(self, request, pk=None):

        insight = Insight.get(pk)
        request.data.pop('user')
        insight.__dict__.update(**request.data)

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
            insights = Insight.search(user=user, personal=False)

            return self.respond_ok(self.log_msg, self.request, self.serializer(insights, return_params_dict).data)

        except Exception as exception:
            return self.__class__.respondToException(exception, self.log_msg, self.request)

    def serializer(self, objs, return_params_dict):
        if 'top_10_keywords' in return_params_dict:
            return InsightWithKeywordsSerializer(objs, many=True)
        else:
            return InsightSerializer(objs, many=True)



from social.apps.django_app.utils import psa, load_strategy

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer


@psa()
def register_by_access_token(request, backend):
    print(backend)
    backend = request.strategy.backend
    # Split by spaces and get the array
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'token':
        msg = 'No token header provided.'
        return msg

    if len(auth) == 1:
        msg = 'Invalid token header. No credentials provided.'
        return msg

    access_token = auth[1]

    user = backend.do_auth(access_token)

    return user


@psa()
def auth_by_token(request, backend):
    backend = request.backend

    user=request.user
    user = backend.do_auth(
        access_token=request.data.get('access_token'),
        user=user.is_authenticated() and user or None
        )
    if user and user.is_active:
        return user# Return anything that makes sense here
    else:
        return None

# Pour une vraie integration au rest framework
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Accepte un backend en parametre : 'auth' pour un login / pass classique
    def post(self, request):
        auth_token = request.data.get('access_token', None)
        backend = request.data.get('backend', None)

        if auth_token and backend:
            try:
                user = auth_by_token(request, backend)
            except Exception as err:
                return Response(str(err), status=400)
            if user:
                strategy = load_strategy(request=request)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'key': token.key})
            else:
                return Response("Bad Credentials", status=403)
        else:
            return Response("Bad request", status=400)

class ObtainUser(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Renvoi le user si le token est valide
    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        if request.META.get('HTTP_AUTHORIZATION'):

            auth = request.META.get('HTTP_AUTHORIZATION').split()

            if not auth or auth[0].lower() != b'token' or len(auth) != 2:
                msg = 'Invalid token header. No credentials provided.'
                return Response(msg, status=status.HTTP_401_UNAUTHORIZED)

            token = Token.objects.get(key=auth[1])
            if token and token.user.is_active:
                return Response({'id': token.user_id, 'name': token.user.username, 'firstname': token.user.first_name, 'userRole': 'user', 'token': token.key})
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class ObtainLogout(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    # Logout le user
    def get(self, request):
        return Response({'User': ''})