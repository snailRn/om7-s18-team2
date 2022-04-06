from django.shortcuts import render, redirect
from authentication.models import CustomUser
from author.models import Author

from authentication.forms import CustomUserForm
from author.forms import AuthorForm


import datetime
import pytz

def authors(request):
    context = Author.get_all()
    title = 'author'
    content = 'All authors'
    return render(request, 'author/base_author.html', {'title': title, 'content': content, 'context': context})

def add_author_info(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            user = Author.objects.get(pk=id)
            form = AuthorForm(instance=user)
        return render(request, 'author/add_author.html', {'form': form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            user = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect('base_author')

def delete_author(request, id=0):
    user = Author.objects.get(pk=id)
    if user:
        user.delete()
    context = Author.get_all()
    title = 'authors'
    content = 'All authors'
    return render(request, 'author/base_author.html', {'title': title, 'content': content, 'context': context})



