from django.urls import path, include
from project.views import TopicListView
from accounts.views import SignUpView




urlpatterns = [
    path('list_of_topics/', TopicListView.as_view(), name='accounts'),
    path('signup/', SignUpView.as_view(), name='templates-signup-page'),
    path('accounts/', include('django.contrib.auth.urls')),
]
