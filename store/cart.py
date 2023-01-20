from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from store.models import *
from django.contrib.auth.decorators import login_required


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            prod_check = Product.objects.get(id=prod_id)
            if (prod_check):
                if (Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': 'product already in cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if prod_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': 'product added successfully'})
                    else:
                        return JsonResponse({'status': 'only ' + str(prod_check.quantity) + " quantity available"})
            else:
                return JsonResponse({'status': 'no such product found'})
        else:
            return JsonResponse({'status': 'login to continue'})
    return redirect('/')


@login_required(login_url='login-page')
def myCart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, 'cart.html', context)


def updateCart(request):
    if request.method == 'POST':
        prod_id_str = request.POST.get('product_id')
        prod_id = int(prod_id_str)
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart =Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':'updated successfully'})


    return redirect('/')


def deleteItem(request):
    if request.method == 'POST':
        prod_id_str = request.POST.get('product_id')
        prod_id = int(prod_id_str)
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitems = Cart.objects.get(product_id= prod_id,user=request.user)
            cartitems.delete()
        return JsonResponse({'status':"deleted successfullu"})
    return redirect('/')