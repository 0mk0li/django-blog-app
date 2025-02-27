# from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # return HttpResponse("Hello! I am homepage.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("I am about page")
    return render(request, 'about.html')
