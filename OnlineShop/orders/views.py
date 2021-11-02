from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Order, OrderItem, Coupon
from cart.cart import Cart
from shop.models import Product
from django.http import HttpResponse,Http404
from suds.client import Client
from django.contrib import messages
from .forms import CouponForm
from django.urls import reverse
from azbankgateways import bankfactories,models as bank_models,default_settings as settings
import logging
import time
# Create your views here.


@login_required
def order_create(request):
    cart = Cart(request)
    print(">>>>>>>>>>>>>>", cart)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        x = Product.objects.get(name=item['product'])
        x.numbers = x.numbers - item['quantity']
        x.save()
    cart.clear()
    return redirect('orders:detail', order.id)


def show_orders(request):
    user = request.user
    ords = user.orders.all()
    context = {
        'orders': ords,
    }
    return render(request, 'orders/all_order.html', context)


def show_detail_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    item = OrderItem.objects.filter(order=order)
    context = {
        'item': item,
        'order': order,
    }
    return render(request, 'orders/detail_orders.html', context)


@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'orders/order.html', context)


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
        except Coupon.DoesNotExist:
            messages.error(request, 'this coupon is invalid.', 'danger')
            return redirect('orders:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
        return redirect('orders:detail', order_id)


