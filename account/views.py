from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        email = request.POST['email']
        password2 = request.POST['password2']
        
        if password1!=password2:
            messages.info(request, 'Password doesnt match with confirmed password')
            context = {
                messages : messages
            }
            return render(request, template_name='account/register.html',context=context)
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            context = {
                messages : messages
            }
            return render(request, template_name='account/register.html',context=context)
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return HttpResponseRedirect(reverse('account:signin'))
    else:
        return render(request,template_name='account/register.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user =  authenticate(email=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            context = {
                user : user
            }
            return render(request, template_name='account/home.html', context=context)
        else:
            messages.info(request, 'Incorrect Email or password')
            context = {
                messages : messages
            }
            return render(request, template_name='account/signin.html',context=context)
    else:
        return render(request, template_name= 'account/signin.html')
    
            
    

def signout(request):
    pass

def home(request):
    pass