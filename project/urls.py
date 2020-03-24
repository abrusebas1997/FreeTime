from django.urls import path, include
from project.views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView, Home, food_image_view, display_food_images, FoodDetailView, FoodUpdateView, FoodDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('list_of_topics/', TopicListView.as_view(), name='topic-list-project'),
    path('image_upload/', food_image_view, name = 'image_upload'),
    path('food_images/', display_food_images, name = 'foods'),
    path('food_detail/<int:pk>/', FoodDetailView.as_view(), name='food-details-project'),
    path('edit/<int:pk>/', FoodUpdateView.as_view(), name='food-update-project'),
    path('delete/<int:pk>', FoodDeleteView.as_view(), name='food-delete-project'),
    path('new_project/', TopicCreateView.as_view(), name='topic-create-project'),
    path('<str:slug>/', TopicDetailView.as_view(), name='topic-details-project'),
    path('edit/<int:pk>/', TopicUpdateView.as_view(), name='topic-update-project'),
    path('delete/<int:pk>', TopicDeleteView.as_view(), name='topic-delete-project'),




]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
