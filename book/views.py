from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Book


def all_book(request):
    context = Book.get_all()
    return render(request, 'book/all_book.html', {'context': context})

def book_by_id(request, id=0):
    context = Book.objects.get(pk=id)
    return render(request, 'book/about_book.html', {'context': context})