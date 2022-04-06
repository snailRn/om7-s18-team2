from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order
from order.forms import OrderForm 

import datetime
import pytz

def not_on_time(request):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    title = 'order selection'
    content = 'Selected with delay'
    context = Order.get_not_returned_books()
    return render(request, 'order/not_on_time.html', {'title': title, 'content': content, 'context': context})

def all_orders(request):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    title = 'All orders'
    content = 'Orders'
    context = Order.objects.all().order_by('id')
    return render(request, 'order/all_orders.html', {'title': title, 'content': content, 'context': context})


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
    title = 'order selection'
    content = f'Selected all orders by user.id = {id}'    
    return render(request, 'order/books_on_hands.html', {'title': title, 'content': content, 'context': context})

def add_order_info(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(instance=order)
        
        return render(request, 'order/order_info.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
    return redirect('all_orders')

def close_order(request, id=0):
    order = Order.objects.get(pk=id)
    order.end_at = datetime.datetime.now()
    order.save()
    return redirect('all_orders')



    # plated_end_at = datetime.datetime.now(tz=pytz.utc) + datetime.timedelta(days=15)
        #     &emsp; <label for="plated_end_at">plated_end_at:</label>
        # {{form.plated_end_at}}<br>
        # <br>