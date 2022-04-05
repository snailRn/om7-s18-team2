from cmath import cos
from django.shortcuts import render, redirect
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from authentication.forms import CustomUserForm

import datetime
import pytz

def users(request):
    context = CustomUser.get_all()
    title = 'users'
    content = 'all users'
    return render(request, 'authentication/users.html', {'title': title, 'content': content, 'context': context})

def add_user_info(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CustomUserForm()
        else:
            user = CustomUser.objects.get(pk=id)
            form = CustomUserForm(instance=user)
        return render(request, 'authentication/userinfo.html', {'form': form})
    else:
        if id == 0:
            form = CustomUserForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=id)
            form = CustomUserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect('users')




def add_info(request):
    try:
        user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='Іван',
                                middle_name='',
                                last_name='Франко')
        user.save()
        user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='Леся',
                                    middle_name='',
                                    last_name='Українка')
        user_free.save()

        author1 = Author(id=101, name="Тарас", surname="Шевченко", patronymic="Григорович")
        author1.save()

        author2 = Author(id=102, name="Іван", surname="Котляревський", patronymic="Петрович")
        author2.save()

        book1 = Book(id=1, name="Кобзар", description="Опис книжки Кобзар", count=5)
        book1.save()
        book1.authors.add(author1)
        book1.save()

        book2 = Book(id=2, name="Енеїда", description="Опис книжки Енеїда")
        book2.save()
        book2.authors.add(author2)
        book2.save()

        book3 = Book(id=103, name="Автобіографії", description="Автобіографії", count=11)
        book3.save()
        book3.authors.add(author1)
        book3.authors.add(author2)
        book3.save()

        TEST_DATE = datetime.datetime(2023, 4, 10, 12, 00, tzinfo=pytz.utc)
        TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)

        order1 = Order(id=51, user=user, book=book1, plated_end_at=TEST_DATE)
        order1.save()
        order2 = Order(id=52, user=user, book=book2, plated_end_at=TEST_DATE)
        order2.save()
        order3 = Order(id=53, user=user, book=book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE)
        order3.save()  
    except: 
        pass
    finally:    
        return render(request, 'library/index.html')
