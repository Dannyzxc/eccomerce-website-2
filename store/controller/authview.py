from django.shortcuts import render,redirect
from django.contrib import messages
# from .models import *
from store.forms import CustomUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as loger
from django.contrib.auth import logout as logouty


def register(request):
          form = CustomUserForm()
          if request.method == 'POST':
                    form = CustomUserForm(request.POST)
                    if form.is_valid():
                              form.save()
                              messages.success(request,"registered successfully!  login to continue")
                              return redirect('/login')
          context = {'form':form}
          return render(request,'auth/register.html',context)

def loginpage(request):
          if request.user.is_authenticated:
                    messages.warning(request,'you are already login ')
                    return redirect('/')
          else:
                    if request.method == 'POST':
                              name = request.POST.get('username')
                              password = request.POST.get('password')

                              user = authenticate(request,username=name,password=password)

                              if user is not None:
                                        loger(request,user) 
                                        messages.success(request,"loged in successfully")
                                        return redirect('/')

                              else:
                                        messages.error(request,'invalid username and password')
                                        return redirect('/login')
                    return render(request,"auth/login.html")

def logoutpage(request):
          if request.user.is_authenticated:
                    logouty(request)
                    messages.success(request,'logout succesfully')
          return redirect('/')

          