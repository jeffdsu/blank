from rest_framework import serializers
from .models import MediumType, Contributor, Checkout, Insight, Medium, Keyword, WordToIgnore, MediumContribution, ContributionType
from django.contrib.auth.models import User

class ContributionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionType
        fields = '__all__'

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        depth = 2

class MediumContributionSerializer(serializers.ModelSerializer):
    contributor = ContributorSerializer()
    type = ContributionTypeSerializer()
    class Meta:
        model = MediumContribution
        #fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        #fields = '__all__'

class MediumSerializer(serializers.ModelSerializer):

    contributions = MediumContributionSerializer(many=True)
    top_10_keywords = serializers.SerializerMethodField()

    def get_top_10_keywords(self, medium):
        keywords = Keyword.get_top_10_keywords(medium)
        return KeywordSerializer(keywords, many=True).data

    class Meta:
        model = Medium
        fields = '__all__'
        depth = 2
        lookup_field = 'type__name'
        extra_kwargs = {
            'url': {'lookup_field': 'type__name'}
        }



class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        #fields = '__all__'


class InsightWithKeywordsSerializer(serializers.ModelSerializer):

    related_medium_top_10_keywords = serializers.SerializerMethodField()
    related_medium_type = serializers.SerializerMethodField()

    def get_related_medium_type(self, insight):
        return insight.medium.type.name

    def get_related_medium_top_10_keywords(self, insight):
        medium = Medium.get(id=insight.medium.id)
        keywords = Keyword.get_top_10_keywords(medium)


        return KeywordSerializer(keywords, many=True).data

    class Meta:
        model = Insight

class InsightSerializer(serializers.ModelSerializer):

    medium_type = serializers.SerializerMethodField()

    def get_medium_type(self, insight):
        return insight.medium.type.name

    class Meta:
        model = Insight
        #fields = '__all__'


class MediumTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumType




class WordToIgnoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordToIgnore
        #fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        write_only_fields = ('password',)

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')