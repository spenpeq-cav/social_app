from django.urls import path
from .views import (
    profile_test_view, 
    MyProfileData, 
    MyProfileView,
)

app_name = 'profiles'

urlpatterns = [
    path('my/', MyProfileView.as_view(), name="my-profile-view"),
    path('my-profile-json/', MyProfileData.as_view(), name="my-profile-json"),
    path('test/', profile_test_view, name="profile-test"),
]