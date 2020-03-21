from django.urls import path

from api.views import TopicList, TopicDetail

urlpatterns = [
    path('topic/', TopicList.as_view(), name='topic_list'),
    path('topic/<int:pk>', TopicDetail.as_view(), name='topic_detail')
]
