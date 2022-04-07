from django import forms
from order.models import Order

import datetime

class OrderForm(forms.ModelForm):   
    plated_end_at = forms.DateTimeField(initial= datetime.datetime.now() + datetime.timedelta(days=15)) 
    class Meta:
        model = Order
        fields = ['plated_end_at','user','book']
    labels = {
        'user' : 'User',
        'book' : 'Book',
        'plated_end_at' : 'plated_end_at',
    }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.id} {obj.first_name} {obj.last_name}'
        self.fields['book'].label_from_instance = lambda obj: f'{obj.id} {obj.name}'

        

