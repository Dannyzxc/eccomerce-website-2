from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    cate = Category.objects.filter(status=0)
    trend = Product.objects.filter(trending=1)
    context = {'cate': cate, 'trend': trend}
    return render(request, 'index.html', context)


def product(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        things = Product.objects.filter(Category__slug=slug)
        Category_name = Category.objects.filter(slug=slug).first()
        context = {'things': things, 'Category_name': Category_name}
        return render(request, 'store.html', context)
    else:
        messages.warning(request, 'no such category found')
        return redirect('/')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            things = Product.objects.filter(slug=prod_slug, status=0).first()

            context = {'things': things}
        else:
            messages.error(request, 'no such product found')
            return redirect('/')
    else:
        messages.error(request, 'no such category found')
        return redirect('/')
    return render(request, 'product.html', context)
