import requests
from django.shortcuts import render
from .serializers import UserSerializer, StatusSerializer, OrderSerializer
from main.models import User, Status, Order
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from main.views import URL, GET_PATH_URL, send_message_deliverer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]

    @action(methods=["get"], detail=False)
    def check_user(self, request):
        tg_id = request.GET.get("tg_id", None)
        user = User.objects.filter(tg_id=tg_id)
        if user.exists():
            return Response("Appear", 200)
        else:
            return Response("Disappear", 400)

    @action(methods=["get"], detail=False)
    def change_status(self, request):
        status_id = request.GET.get("status")
        order_id = request.GET.get("order")

        order = Order.objects.get(id=order_id)
        order_last = Status.objects.all().last()
        order.status_id = status_id
        order.save()
        print(order_last.id, order.status_id)
        if int(order_last.id) != int(order.status_id):
            send_message_deliverer(order.status.id, order.id, order.deliverer.tg_id)

        return Response({"message": "Success"}, status=200)

    @action(methods=["get"], detail=False)
    def change_price(self, request):
        price = request.GET.get("price")
        order_id = request.GET.get("order_id")

        order = Order.objects.get(id=order_id)
        order.get_price = price
        order.save()

        return Response("Save price", status=200)

    @action(methods=["post"], detail=False)
    def post(self, request):
        user = request.data.get("user", None)
        order = request.data.get("order", None)
        print(user, order)
        if User.objects.filter(tg_id=user['tg_id']).exists():
            user_instance = User.objects.get(tg_id=user["tg_id"])
            print(user_instance)
        else:
            user_instance = User.objects.create(
                **user
            )
        file_id = order.get("image_file_id", None)
        text = order.get("text_recipies", None)
        status = Status.objects.all().first()
        print(text, file_id)
        if file_id is not None:
            print("image is not")

            url = f"{GET_PATH_URL}{file_id}"
            response = requests.request("GET", url)
            res = response.json()
            file_path = res['result'].get("file_path", None)
            order_instance = Order.objects.create(
                image_recipies=file_path,
                user=user_instance,
                status=status
            )
        elif text is not None:
            print("text is not")
            order_instance = Order.objects.create(
                text_recipies=text,
                user=user_instance,
                status=status
            )
        return Response("data")


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # permission_classes = [IsAuthenticated]


class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # permission_classes = [IsAuthenticated]


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
