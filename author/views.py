from django.shortcuts import render
from book.models import Book
from author.models import Author


def author_books(request, id=0):
    authors_book = []

    for book in Book.objects.all():
        for author in book.authors.all():
            if author.id == id: authors_book.append(book)
    title = 'books'
    content = f'Selected all book by author id = {id}'    
    return render(request, 'book/all_book.html', {'title': title, 'content': content, 'context': authors_book})
