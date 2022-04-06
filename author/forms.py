from .models import Author
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic',

        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)