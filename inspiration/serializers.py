from rest_framework import serializers
from .models import MediumType, Contributor, Checkout, Insight, Medium, Keyword, WordToIgnore
from django.contrib.auth.models import User


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = '__all__'
        depth = 2
        lookup_field = 'type__name'
        extra_kwargs = {
            'url': {'lookup_field': 'type__name'}
        }

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
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


class MediumTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumType

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        #fields = '__all__'


class WordToIgnoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordToIgnore
        #fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        write_only_fields = ('password',)