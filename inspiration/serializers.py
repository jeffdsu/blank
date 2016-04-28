from rest_framework import serializers
from .models import Book, Author, Checkout, Insight, Medium, BookKeywords


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