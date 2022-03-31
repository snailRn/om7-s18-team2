from django.shortcuts import render
from order.models import Order

def not_on_time(request):
    #context = author_list
    #return render(request, 'library/not_on_time.html', {'context': context})
    context = Order.get_not_returned_books()
    return render(request, 'order/not_on_time.html', {'context': context})
    #a= {'id': 15, 'age': 28}
    #b = {'id': 16, 'age': 29}
    #c = {'id': 17, 'age': 30}
    #context = [a,b,c]
    #context = []
    #return render(request, 'library/not_on_time.html', {'context': context})
