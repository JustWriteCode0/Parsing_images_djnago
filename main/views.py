import self as self
from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Url
from .service import *
from django.http import HttpResponse


def main(request):
    posts = Url.objects.all()
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result_page')
    else:
        form = UrlForm()
        return render(request, 'main/main.html', {'form': form, 'posts': posts})


def alldata(request):
    image = scraping().get_images()
    if request.method == 'POST':
        return redirect('home_page')
    else:
        return render(request, 'main/response.html', {'image': image})
