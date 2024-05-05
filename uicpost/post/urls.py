from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(template_name='post/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='post/logout.html'), name='logout'),
    path("register/", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("delivery/", views.delivery, name="delivery"),
    path("order_list/", login_required(views.OrderListView.as_view()), name="order_list"),
    path("order_detail/", views.order_detail, name="order_detail"),
    path("calculate_price/", views.calculate_price, name="calculate_price"),
]