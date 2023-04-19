from django.shortcuts import render, HttpResponse
from .models import Order


def order_list(request):
    order = Order.objects.all()
    return HttpResponse(order)
