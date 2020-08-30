from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .form import NoticeForm, NoticeImageForm
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
