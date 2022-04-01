from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Book


def all_book(request, sort='id'):
    context = Book.get_all()
    if sort == 'id': context.sort(key=lambda book: book.id)
    if sort == 'count': context.sort(key=lambda book: book.count)
    if sort == 'name_asc': context.sort(key=lambda book: book.name, reverse=False)
    if sort == 'name_desc': context.sort(key=lambda book: book.name, reverse=True)
    return render(request, 'book/all_book.html', {'context': context})