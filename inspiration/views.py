from .models import Book, Author, Checkout, Insight, BookKeywords, WordsToIgnore, Medium
from .serializers import BookSerializer, AuthorSerializer, CheckoutSerializer, InsightSerializer, MediumSerializer
from rest_framework import viewsets
import string

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

class InsightViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = InsightSerializer

    def list(self, request, books_pk=None):


        insights = Insight.objects.filter(book=books_pk, valid=True)
        return Response(InsightSerializer(insights, many=True).data)

    def create(self, request, books_pk=None):

        insight_dict = dict()
        insight_dict['user'] = request.user
        insight_dict['lesson'] = request.data['lesson']
        insight_dict['book_id'] = books_pk
        insight_dict['checkout'] = request.data['checkout'] if 'checkout' in request.data else None

        insight = Insight(**insight_dict)
        insight.save()
        insight.save()

        return Response(InsightSerializer(insight).data)

    @detail_route(methods=['put'])
    def validate (self, request, books_pk=None, pk=None):
        '''
        Used to validate a specific insight.  This will call the parse lesson function.
        :param request:
        :param books_pk:
        :return:
        '''

        try:
            book = Book.get(books_pk)
            insight = Insight.get(pk)
        except Exception as exception:
            return exception.args[0]

        # if the insight is already set to true, don't do anything
        # should this be a 200 response?
        if insight.valid == True:
            return self.respond_ok(InsightSerializer, insight)

        # Add parsed words to insight keywords
        list_of_found_words = self.parse_lesson(insight.lesson)

        # this should do its magic
        self.understand(book, list_of_found_words)

        #insight.valid = True
        #insight.save()
    def understand(self, book, list_of_found_words):
        list_of_known_keywords = BookKeywords.search(book)

    def parse_lesson(self, lesson):

        list_of_words_to_ignore = WordsToIgnore.objects.all()
        parsed_list = []
        split_list = lesson.split()

        remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        split_list = [s.translate(remove_punctuation_map) for s in split_list]

        for word in split_list:
            word = word.translate(string.punctuation)

        # This might need a better way later
        dict_of_words_to_ignore = {list_of_words_to_ignore[i]: 1 for i in range(len(list_of_words_to_ignore))}

        #someone tell me if there is a better way to write this
        for word in split_list:
            word_lc = word.lower()
            if word_lc not in dict_of_words_to_ignore:
                parsed_list.append(word_lc)

        return parsed_list

