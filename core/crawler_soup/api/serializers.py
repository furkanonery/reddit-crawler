from rest_framework import serializers
from crawler_soup.models import Subreddits

class SubredditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddits
        fields = '__all__'