from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from project.models import Topic
from api.serializers import TopicSerializer


class TopicList(APIView):
    def get(self, request):
        topics = Topic.objects.all()[:20]
        data = TopicSerializer(topics, many=True).data
        return Response(data)

class TopicDetail(APIView):
    def get(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        data = TopicSerializer(topic).data
        return Response(data)
