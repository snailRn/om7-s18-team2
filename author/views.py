from django.shortcuts import render
from book.models import Book

def author_books(request, id=0):
    authors_book = []

    for book in Book.objects.all():
        for author in book.authors.all:
            if author.id == id: authors_book.append(book)
    title = 'books '
    content = 'Selected all author book'    
    return render(request, 'book/all_book.html', {'title': title, 'content': content, 'context': authors_book})
