from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order
from book.models import Book


def index(request):
    return render(request, 'library/index.html')

def all_book(request):
    context = Book.get_all()
    return render(request, 'library/all_book.html', {'context': context})


def not_on_time(request):
    #context = author_list
    #return render(request, 'library/not_on_time.html', {'context': context})
    context = Order.get_not_returned_books()
    return render(request, 'library/not_on_time.html', {'context': context})
    #a= {'id': 15, 'age': 28}
    #b = {'id': 16, 'age': 29}
    #c = {'id': 17, 'age': 30}
    #context = [a,b,c]
    #context = []
    #return render(request, 'library/not_on_time.html', {'context': context})
