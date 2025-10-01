from django.urls import path
from .views import page_view_signup


urlpatterns = [
    path("api/signup/", page_view_signup.as_view(), name = 'signup')
]