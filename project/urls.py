from django.urls import path, include
from project.views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView, Home


urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('list_of_topics/', TopicListView.as_view(), name='topic-list-project'),
    path('new_project/', TopicCreateView.as_view(), name='topic-create-project'),
    path('<str:slug>/', TopicDetailView.as_view(), name='topic-details-project'),
    path('edit/<int:pk>/', TopicUpdateView.as_view(), name='topic-update-project'),
    path('delete/<int:pk>', TopicDeleteView.as_view(), name='topic-delete-project'),

]
