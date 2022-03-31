from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order


def index(request):
    return render(request, 'library/index.html')

def not_on_time(request):
    context = Order.objects.all()
    return render(request, 'library/not_on_time.html', {'context': context})
    #context = ['sasha','tolja',2,3]
    #context = []
    #return render(request, 'library/not_on_time.html', {'context': context})
