from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from django.http.response import JsonResponse


@login_required(login_url='login-page')
def checkout(request):
    raw_cart = Cart.objects.filter(user=request.user)
    for item in raw_cart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartitems = Cart.objects.filter(user=request.user)

    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems': cartitems, 'total_price': total_price, 'userprofile': userprofile}
    return render(request, 'checkout.html', context)


@login_required(login_url='login-page')
def placeholder(request):
    if request.method == 'POST':

        # create a default user
        current_user = User.objects.filter(id=request.user.id).first()
        if not current_user.first_name:
            current_user.first_name = request.POST.get('firstname')
            current_user.last_name = request.POST.get('firstname')
            current_user.save()

        # create a default user
        if not (Profile.objects.filter(user=request.user)):
            user_profile = Profile()
            user_profile.user = request.user
            user_profile.phone = request.POST.get('phone')
            user_profile.email = request.POST.get('email')
            user_profile.address = request.POST.get('address')
            user_profile.state = request.POST.get('state')
            user_profile.city = request.POST.get('city')
            user_profile.save()

        # save data to database
        newOrder = Order()
        newOrder.user = request.user
        newOrder.firstname = request.POST.get('firstname')
        newOrder.lastname = request.POST.get('lastname')
        newOrder.phone = request.POST.get('phone')
        newOrder.email = request.POST.get('email')
        newOrder.address = request.POST.get('address')
        newOrder.state = request.POST.get('state')
        newOrder.city = request.POST.get('city')

        newOrder.payment_mode = request.POST.get('paymode')
        newOrder.payment_id = request.POST.get('payment_id')

        # get total amount for payment
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.price * item.product_qty
        newOrder.total_price = cart_total_price

        # update tracking id
        track_num = 'track' + str(random.randint(111111, 999999))
        while (Order.objects.filter(tracking_num=track_num)) is None:
            track_num = 'track' + str(random.randint(111111, 999999))
        newOrder.tracking_num = track_num
        newOrder.save()

        neworder_items = (Cart.objects.filter(user=request.user))
        for item in neworder_items:
            OrderItem.objects.create(
                order=newOrder,
                product=item.product,
                price=item.product.price,
                quantity=item.product_qty,
            )

            # to decrease the product quantity from available stock

            order_product = Product.objects.filter(id=item.product_id).first()
            order_product.quantity = order_product.quantity - item.product_qty
            order_product.save()

        Cart.objects.filter(user=request.user).delete()
        # messages.success(request, "your order has been placed successfully")

    payMode = request.POST.get('paymode')
    if payMode == "paid by Razorpay":
        return JsonResponse({'status': "your order has been placed successfully"})
    else:
        messages.success(request, "your order has been placed successfully")

    return redirect('/')


@login_required(login_url='login-page')
def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    cart_total_price = 0
    for item in cart:
        cart_total_price = cart_total_price + item.product.price * item.product_qty

    context = {'cart_total_price': cart_total_price}
    return JsonResponse(context)


def myorders(request):
    return HttpResponse("my orders page")
