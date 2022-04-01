from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Book


def all_book(request, sort='id'):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    context = Book.get_all()
    if sort == 'id':
        context.sort(key=lambda book: book.id)
        title = 'sort by id'
        content = 'Selected by book id'
    if sort == 'count':
        context.sort(key=lambda book: book.count)
        title = 'sort by count'
        content = 'Selected by book count'
    if sort == 'name_asc':
        context.sort(key=lambda book: book.name, reverse=False)
        title = 'sort by name_asc'
        content = 'Selected by book name in ascending mode'
    if sort == 'name_desc':
        context.sort(key=lambda book: book.name, reverse=True)
        title = 'sort by name_desc'
        content = 'Selected by book name in descending mode'

    return render(request, 'book/all_book.html', {'title': title, 'content': content, 'context': context})

