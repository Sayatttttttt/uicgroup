from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Role, Order, Filial
from .forms import OrderForm
from .map_functions import calculate_order


class OrderListView(ListView):
    model = Order
    template_name = 'post/order_list.html'
    context_object_name = 'orders'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Order.objects.filter(filial_send=user.role.filial).order_by('-date_posted') 

def order_detail(request):
    order_id = request.GET.get('orderid', '')
    if not order_id and not order_id.isdigit():
        return render(request, 'post/order_detail.html', {'order': None})
    try:
        order = Order.objects.get(id=int(order_id))
    except:
        messages.error(request, 'Order not found')
        return render(request, 'post/order_detail.html', {'order': None})
    return render(request, 'post/order_detail.html', {'order': order})

def calculate_price(request):
    filials = Filial.objects.all()
    adresses = dict([(str(f.pk), f.filial) for i, f in enumerate(filials, start=1)])
    print(request.GET)
    print(adresses)
    pick_up_address = adresses[request.GET.get('pick_up_address')]
    drop_off_address = adresses[request.GET.get('drop_off_address')]
    print(pick_up_address, drop_off_address)
    # car_type = request.GET.get('car_type')
    calculated_price, distance_km, pick_coords, drop_coords = calculate_order(pick_up_address, drop_off_address, car_type='standart')
    try:
        calculated_price, distance_km, pick_coords, drop_coords = calculate_order(pick_up_address, drop_off_address, car_type='standart')
    except Exception as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse({'price': calculated_price, 'distance': distance_km, 'pick_coords': pick_coords, 'drop_coords': drop_coords})

def delivery(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['filial_send'] != form.cleaned_data['filial_receive']:
                order = Order(**form.cleaned_data)
                order.save()
                return render(request, 'post/delivery.html', {'form': form})
            else:
                messages.error(request, 'Filials must be different')
    return render(request, 'post/delivery.html', {'form': OrderForm()})

def index(request):
    return render(request, 'post/index.html')

def login(request):
    return render(request, 'post/login.html')

def register(request):
    return render(request, 'post/register.html')

def about(request):
    return render(request, 'post/about.html')