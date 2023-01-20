from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from store.models import *
# from store.forms import CustomUserForm
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as loger
# from django.contrib.auth import logout as logouty
import json
from django.contrib.auth.decorators import login_required



@login_required(login_url='login-page')
def wishList(request):
    wishList = Wish_List.objects.filter(user=request.user)
    context = {'wishList':wishList}
    return render(request, 'wishlist.html', context)



def addtowish(request):
    if request.method == 'POST':
        if request.user.is_authenticated:

            prod_id = int(request.POST.get('product_id'))
            prod_check = Product.objects.get(id=prod_id)
            if (prod_check):
                if (Wish_List.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': 'product already in wishlist'})
                else:

                    Wish_List.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': 'product added successfully'})
               
            else:
                return JsonResponse({'status': 'no such product found'})
        else:
            return JsonResponse({'status': 'login to continue'})
    return redirect('/')



def deleteWishItem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if (Wish_List.objects.filter(user=request.user, product_id=prod_id)):
                wishlist_item = Wish_List.objects.get(user=request.user,product_id=prod_id)
                wishlist_item.delete()
                return JsonResponse({'status': 'product removed from wishlist'})
            else:
                return JsonResponse({'status': 'product not found'})
        else:
            return({'status':"login to continue"})
            
    return redirect('/')

