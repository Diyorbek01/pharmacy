from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order-list", views.order_list, name="order-list"),
    path("user-list", views.user_list, name="user-list"),
    path("deliverer-list", views.deliverer_list, name="deliverer-list"),
    path("create-user", views.create_user, name="create-user"),
]