from django.urls import path
from .views import profile_test_view

app_name = 'profiles'

urlpatterns = [
    path('test/', profile_test_view, name='profile-test')
]