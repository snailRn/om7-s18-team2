from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order
from book.models import Book
from authentication.models import CustomUser
from author.models import Author




def options(request):
    context = {'all_books': Book.get_all(), 'all_users':CustomUser.get_all(), 'all_authors':Author.get_all()}
    return render(request, 'library/options.html', context)

def index(request):
    return render(request, 'library/index.html')
