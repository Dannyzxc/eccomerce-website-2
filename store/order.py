from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from django.http.response import JsonResponse


def myOrderDetails(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'order.html', context)


def orderOverview(request, t_no):
    orders = Order.objects.filter(user=request.user).filter(tracking_num=t_no).first()
    orderItem = OrderItem.objects.filter(order=orders)
    context = {'orders': orders, 'orderItem': orderItem}
    return render(request, 'ordersum.html', context)


