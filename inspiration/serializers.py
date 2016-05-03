from rest_framework import serializers
from .models import Book, Author, Checkout, Insight, Medium, BookKeywords, WordsToIgnore
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        depth = 2

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        #fields = '__all__'

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        #fields = '__all__'

class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium

class BookKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookKeywords
        #fields = '__all__'


class WordsToIgnoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsToIgnore
        #fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        write_only_fields = ('password',)