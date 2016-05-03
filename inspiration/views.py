from .models import Book, Author, Checkout, Insight, BookKeywords, WordsToIgnore, Medium
from .serializers import BookSerializer, AuthorSerializer, CheckoutSerializer, InsightSerializer, MediumSerializer, BookKeywordsSerializer, WordsToIgnoreSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView

class MediumViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Medium.objects.all()
    serializer_class = MediumSerializer

class BookKeywordsViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = BookKeywords.objects.filter()
    serializer_class = BookKeywordsSerializer

    def list(self, request, books_pk=None):

        book = Book.get(books_pk)

        format_qp = self.request.query_params.get('style', None)
        kwargs = dict()
        kwargs['style'] = format_qp
        book_keywords = BookKeywords.search(book, **kwargs)
        print(len(book_keywords))

        #if format_qp is not None:

        return Response(BookKeywordsSerializer(book_keywords, many=True).data)

class BookViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)

class AuthorViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CheckoutViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class BookInsightViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = InsightSerializer

    def list(self, request, books_pk=None):
        try:
            book = Book.get(books_pk)

            random_top_10_qp = self.request.query_params.get('random_top_10', None)
            if random_top_10_qp is not None:

                keywords = BookKeywords.get_top_10_keywords(book)

                search = dict()
                for keyword in keywords:
                    search['lesson__icontains'] = keyword.word

                insights = Insight.search(book, **search)

                import random

                return Response(InsightSerializer(random.choice(insights)).data)

            else:
                insights = Insight.search(book)

                return Response(InsightSerializer(insights, many=True).data)

        except Exception as exception:
            return exception.args[0]

class InsightViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
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

    #TODO - this should be an admin only api
    @detail_route(methods=['put'])
    def validate (self, request, pk=None):
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
            return exception.args[0]


class WordsToIgnoreViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = WordsToIgnore.objects.all()
    serializer_class = WordsToIgnoreSerializer

    def create(self, request):

        try:
            new_word = WordsToIgnore(word=request.data['word'])
            book_keywords = BookKeywords.admin_search(word=request.data['word'])

            book_keywords.delete()
            new_word.save()

            return Response(WordsToIgnoreSerializer(new_word).data)

        except Exception as exception:
            return exception.args[0]




