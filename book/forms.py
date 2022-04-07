from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['name', 'description', 'count', 'authors']
    labels = {
        'name' : 'Book Name',
        'description' : 'Description',
        'count' : 'Count',
        'authors'  : 'authors',
    }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)