from django.db import models
from django.contrib.auth.models import AbstractUser


USERSTATUS = [
    ("Client","Client"),
    ("Deliverer","Deliverer"),
]

class User(AbstractUser):
    tg_id = models.IntegerField(unique=True,null=True)
    full_name = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    status = models.CharField(max_length=255,choices=USERSTATUS,null=True)
    location = models.CharField(max_length=255,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.full_name)

class Status(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.name)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    price = models.IntegerField(null=True)
    get_price = models.IntegerField(null=True)
    image_recipies = models.ImageField(upload_to="order/",null=True)
    text_recipies = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.price)