from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role']
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
