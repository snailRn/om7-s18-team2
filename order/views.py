from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order

def not_on_time(request):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    title = 'order selection'
    content = 'Selected with delay'
    context = Order.get_not_returned_books()
    return render(request, 'order/not_on_time.html', {'title': title, 'content': content, 'context': context})

def selection_date(request, address = 'all'):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    #context = Order.get_all()
    if address == 'all':
        context = Order.objects.all().order_by('date')
        title = 'order selection'
        content = 'Selected all orders'
    if address == 'created_at':
        context = Order.objects.all().order_by('created_at')
        title = 'order selection'
        content = 'Selected by by created at date'
    if address == 'plated_at':
        context = Order.objects.all().order_by('plated_end_at')
        title = 'order selection'
        content = 'Selected by by plated at date'
    return render(request, 'order/not_on_time.html', {'title': title, 'content': content, 'context': context})

def user_books(request, id=0):
    context = Order.objects.all().filter(user = id)
    print(context)
    title = 'order selection'
    content = 'Selected all orders'    
    return render(request, 'order/books_on_hands.html', {'title': title, 'content': content, 'context': context})

