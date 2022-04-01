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

def selection_date(request, sort='all'):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    context = Order.objects.all()
    if sort == 'all':
        title = 'order selection'
        content = 'Selected all orders'
    if sort == 'created_at':
        context.sort(key=lambda order: order.created_at)
        title = 'order selection'
        content = 'Selected by by created at date'
    if sort == 'plated_at':
        context.sort(key=lambda order: order.plated_end_at)
        title = 'order selection'
        content = 'Selected by by plated at date'

    return render(request, 'order/not_on_time.html, {'title': title, 'content': content, 'context': context})

