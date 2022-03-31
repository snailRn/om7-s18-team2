from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Book


def all_book(request):
    context = Book.get_all()
    return render(request, 'book/all_book.html', {'context': context})