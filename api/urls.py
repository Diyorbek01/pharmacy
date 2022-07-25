from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import UserView,UserDetailView,StatusView,StatusDetailView,OrderView,OrderDetailView

urlpatterns = [
    path('user/',UserView.as_view()),
    path('user/<int:pk>/',UserDetailView.as_view()),
    path('status/',StatusView.as_view()),
    path('status/<int:pk>/',StatusDetailView.as_view()),
    path('order/',OrderView.as_view()),
    path('order/<int:pk>/',OrderDetailView.as_view()),
]
