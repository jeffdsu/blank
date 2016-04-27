from .models import Book, Author, Checkout, Insight, InsightKeywords, WordsToIgnore
from .serializers import BookSerializer, AuthorSerializer, CheckoutSerializer, InsightSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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
        lessons_learned = Insight.objects.filter(book=books_pk)
        return Response(InsightSerializer(lessons_learned, many=True).data)

    def create(self, request, books_pk=None):

        lesson_dict = dict()
        lesson_dict['user'] = request.user
        lesson_dict['lesson_learned'] = request.data['lesson_learned']
        lesson_dict['book_id'] = books_pk
        lesson_dict['checkout'] = request.data['checkout'] if 'checkout' in request.data else None

        lesson = Insight(**lesson_dict)
        lesson.save()

        return Response(InsightSerializer(lesson).data)

    def parse_lesson(self, lesson):

        list_of_words_to_ignore = WordsToIgnore.objects.all()
        parsed_list = []
        split_list = lesson.split()

        # This might need a better way later
        dict_of_words_to_ignore = {list_of_words_to_ignore[i]: 1 for i in range(len(list_of_words_to_ignore))}

        #someone tell me if there is a better way to write this
        for word in split_list:
            word_lc = word.lower()
            if word_lc not in dict_of_words_to_ignore:
                parsed_list.append(word_lc)

        return parsed_list

