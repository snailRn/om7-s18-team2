from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    labels = {
        'first_name' : 'First Name',
        'middle_name' : 'Middle Name',
        'last_name' : 'Last Name',
        'email'  : 'email Name',
        'password'  : 'password',
        'role' : 'Role'
    }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
