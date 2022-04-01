from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order
from book.models import Book


def index(request):
    return render(request, 'library/index.html')
