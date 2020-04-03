
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .Forms import UserForm
from .Forms import UserPost
from .models import user

def home(request):

    return render(request,'Home.html')

def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(Username=username, Password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('post')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'signin.html', {})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('post')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def Post(request):
    context = {}

    # create object of form
    post = UserPost(request.POST or None, request.FILES or None)

    # check if form data is valid
    if post.is_valid():
        # save the form data to model
        post.save()

    context['post'] = post
    return render(request, "Post.html", context)
