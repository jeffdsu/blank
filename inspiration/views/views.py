from inspiration.models import Book, Author, Checkout, Insight, BookKeywords, WordsToIgnore, Medium
from inspiration.serializers import BookSerializer, AuthorSerializer, CheckoutSerializer, InsightSerializer, MediumSerializer, \
    UserSerializer, BookKeywordsSerializer, WordsToIgnoreSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from inspiration.views.InpsiprationBaseViewMixIn import InspirationBaseViewMixIn


class MediumViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Medium.objects.all()
    serializer_class = MediumSerializer


class BookKeywordsViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = BookKeywords.objects.filter()
    serializer_class = BookKeywordsSerializer

    def list(self, request, books_pk=None):
        book = Book.get(books_pk)

        format_qp = self.request.query_params.get('style', None)
        kwargs = dict()
        if format_qp:
            kwargs['style'] = format_qp
        book_keywords = BookKeywords.search(book, **kwargs)
        print(len(book_keywords))

        # if format_qp is not None:

        return Response(BookKeywordsSerializer(book_keywords, many=True).data)


class BookViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)


class AuthorViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CheckoutViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class BookInsightViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = InsightSerializer

    def list(self, request, books_pk=None):
        try:
            book = Book.get(books_pk)

            random_top_10_qp = self.request.query_params.get('random_top_10', None)
            if random_top_10_qp is not None:

                keywords = BookKeywords.get_top_10_keywords(book)

                query = Q(book=book, valid=True)
                keyword_q = Q()

                for keyword in keywords:
                    keyword_q |= Q(lesson__icontains=keyword.word)

                insights = Insight.objects.filter(query & keyword_q)
                for i in insights:
                    print(i.lesson)

                import random

                return Response(InsightSerializer(random.choice(insights)).data)

            else:
                insights = Insight.search(book=book, valid=True)

                return Response(InsightSerializer(insights, many=True).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)

    def create(self, request, books_pk=None):
        try:
            book = Book.get(books_pk)
            user = request.user
            lesson = request.data['lesson']

            temp_insight = Insight(book=book, user=user, lesson=lesson, valid=False)

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

    def create(self, request, books_pk=None):

        insight_dict = dict()
        insight_dict['user'] = request.user
        insight_dict['lesson'] = request.data['lesson']
        insight_dict['book_id'] = books_pk
        insight_dict['checkout'] = request.data['checkout'] if 'checkout' in request.data else None

        insight = Insight(**insight_dict)
        insight.save()

        return Response(InsightSerializer(insight).data)




class WordsToIgnoreViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = WordsToIgnore.objects.all()
    serializer_class = WordsToIgnoreSerializer

    def create(self, request):

        try:

            new_word = WordsToIgnore.search(word=request.data['word'])

            if new_word:
                return WordsToIgnore.respond_already_found(word=request.data['word'])

            new_word = WordsToIgnore(word=request.data['word'])
            book_keywords = BookKeywords.admin_search(word=request.data['word'])

            book_keywords.delete()
            new_word.save()

            return Response(WordsToIgnoreSerializer(new_word).data)

        except Exception as exception:
            return self.__class__.respondToException(exception)


class UserViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    queryset = User.objects.all()
    serializer = UserSerializer()


class AuthorBooksViewSet(viewsets.ModelViewSet, InspirationBaseViewMixIn):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, authors_pk=None):
        try:
            author = Author.get(authors_pk)
            books = Book.search(author=author)

            return Response(BookSerializer(books, many=True).data)

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






