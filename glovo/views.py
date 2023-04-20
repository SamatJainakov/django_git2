from django.shortcuts import render, HttpResponse
from .models import Courier


def courier_list(request):
    couriers = Courier.objects.all()
    return HttpResponse(couriers)
