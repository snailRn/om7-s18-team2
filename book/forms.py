from dataclasses import field
from django import forms
from book.models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
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
        self.fields['authors'].label_from_instance = lambda obj: f'{obj.name} {obj.surname} {obj.patronymic}'
