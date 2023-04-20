from django.shortcuts import render, HttpResponse
from .models import Order, Courier


def order_list(request):
    order = Order.objects.all()
    return HttpResponse(order)


def courier_list(request):
    couriers = Courier.objects.all()
    return HttpResponse(couriers)
