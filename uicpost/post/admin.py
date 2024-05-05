from django.contrib import admin
from .models import Role, Order, Filial

# Register your models here.
admin.site.register([Role, Order, Filial])