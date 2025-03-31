from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsersApi

router = DefaultRouter()

urlpatterns = [
    path('users/', UsersApi.as_view(), name='users'),
    path('users/<int:pk>/', UsersApi.as_view(), name='user_detail'),
]