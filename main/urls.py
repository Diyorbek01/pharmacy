from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order-list/", views.order_list, name="order-list"),
    path("order-list/<str:id>", views.filter_order, name="filter-order"),
    path("order-price/", views.price, name="order-price"),
    path("client-list/", views.user_list, name="client-list"),
    path("deliverer-list/", views.deliverer_list, name="deliverer-list"),
    path("deliverer-status/", views.deliverer_status, name="deliverer-status"),
    path("create-status/", views.status, name="create-status"),
    path("delete-status/<int:id>", views.delete_status, name="delete-status"),
    path("create-user/", views.create_user, name="create-user"),
    path("update-user/<int:id>", views.update_user, name="update-user"),
    path("delete-user/<int:id>", views.delete_user, name="delete-user"),

    path("user-location/<int:id>", views.user_location, name="user-location"),
]