from django.db import models
from django.contrib.auth.models import User


class Filial(models.Model):
    filial = models.CharField(max_length=200)
    
    def __str__(self):
        return self.filial

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.filial} - {self.role}"

class Order(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    father = models.CharField(max_length=200)
    filial_send = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name="filial_send")
    filial_receive = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name="filial_receive")
    status = models.CharField(max_length=200, default="Pending")
    price = models.IntegerField(default=150)
    mass = models.IntegerField(default=None, null=True)
    volume = models.IntegerField(default=None, null=True)
    
    def __str__(self):
        return f"Order number: {self.id}"