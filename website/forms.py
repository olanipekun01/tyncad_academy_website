from .models import *
from django.forms import ModelForm, fields


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone_number', 'description',)