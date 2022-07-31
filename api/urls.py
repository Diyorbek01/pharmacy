from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import UserView,UserDetailView,StatusView,StatusDetailView,OrderView,OrderDetailView
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
# ---------- Partner
router.register('user', UserView)

# urlpatterns = [
#     # path('user/',UserView.as_view()),
#     path('user/<int:pk>/',UserDetailView.as_view()),
#     path('status/',StatusView.as_view()),
#     path('status/<int:pk>/',StatusDetailView.as_view()),
#     path('order/',OrderView.as_view()),
#     path('order/<int:pk>/',OrderDetailView.as_view()),
# ]
