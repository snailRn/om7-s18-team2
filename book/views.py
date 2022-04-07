from audioop import reverse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from book.models import Book
from order.models import Order
from book.forms import BookForm

def book_by_id(request, id=0):
    context = Book.objects.get(pk=id)
    title = 'Book by id'
    content = f'Book by id = {id}'    
    return render(request, 'book/about_book.html', {'title': title, 'content': content, 'context': context})

def all_book(request, sort='id'):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    context = Book.get_all()
    if sort == 'id':
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

def unodered_books(request):
    list_unodered_books = []
    all_books = Book.objects.all()
    all_orders = Order.objects.all()
    for book in all_books:
        ordered_book=0
        for order in all_orders:
            if book.id == order.book.id and order.end_at == None:
                ordered_book += 1
        difference = book.count - ordered_book
        if difference > 0:
            book_dict = {
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'count': book.count,
                'authors': book.authors,
                'difference': difference
                        }
            list_unodered_books.append(book_dict)

    context = list_unodered_books
    title = 'all unordered book'
    content = 'all unordered book'
    return render(request, 'book/unordered_book.html', {'title': title, 'content': content, 'context': context})

def filter_book(request):
    filter_opt = request.GET
    title = 'filtered books'
    content = 'filtered books'
    filter_par = Q(name__icontains=filter_opt.get('book')) & (Q(authors__name__icontains = filter_opt.get('author')) | \
                        Q(authors__surname__icontains = filter_opt.get('author')) | \
                        Q(authors__patronymic__icontains = filter_opt.get('author')) )
    context = Book.objects.filter(filter_par).distinct()
    return render(request, 'book/all_book.html', {'title': title, 'content': content, 'context': context})

def adm_books(request, sort='id'):
    """
    title - name of our page, which you can see in browser when mouse is pointed on web-site
    content - name of selection type
    """
    context = Book.objects.all().order_by('id')
    if sort == 'id':
        title = 'sort by id'
        content = 'admin books'

    return render(request, 'book/adm_books.html', {'title': title, 'content': content, 'context': context})

def add_book(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            order = Book.objects.get(pk=id)
            form = BookForm(instance=order)        
        return render(request, 'book/books_info.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            order = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
    return redirect('adm_books')
    
def delete_book(request, id=0):
    user = Book.objects.get(pk=id)
    if user:
        user.delete()
    return redirect('adm_books')
    