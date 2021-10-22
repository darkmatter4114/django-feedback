from django.contrib import messages
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .form import NoticeForm, NoticeImageForm, NewUserForm
from .models import Notice as NoticeModel
from django.views.generic.edit import CreateView, FormView


def no_log(reques):
    return render(reques, 'no log.html')


def index(request):
    notice = NoticeModel.objects.all
    return render(request, 'index.html', {'notice': notice})


def success_sending(request):
    return render(request, 'notice/successfully.html')


def post_new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES or None)
        # ctx = {'form': form}
        if form.is_valid():
            post = form.save()
            post.save()
            messages.info(request, 'Your message sending is success!')
    else:
        form = NoticeForm()
    return render(request, 'notice/create.html', {'form': form})


class NoticeCreateForm(CreateView):
    model = NoticeModel
    fields = ['name', 'email', 'message', 'pub_date', 'image']
    # template_name = 'create.html'
    # form_class = NoticeForm
    # success_url = '/thanks/'


class NoticeDownloadImageView(FormView):
    form_class = NoticeImageForm
    template_name = ''


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="notice/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="notice/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main")
