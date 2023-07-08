from rest_framework.views import APIView
from rest_framework.response import Response
from crawler_soup.api.serializers import SubredditsSerializer
from crawler_soup.models import Subreddits
from .task import getposts


class SubredditsView(APIView):
    def get(self, request, format=None):

        queryset = Subreddits.objects.all()

        serializer = SubredditsSerializer(queryset, many=True)

        return Response(serializer.data)