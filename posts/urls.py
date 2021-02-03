from django.urls import path
from .views import home_view, posts_view_json

app_name = 'posts'

urlpatterns = [
    path('', home_view, name='home-view'),
    
    # Endpoints
    path('posts-json/', posts_view_json, name='posts-view-json'),
]