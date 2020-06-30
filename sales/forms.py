from django import forms
from .models import Stock, Invoice, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django_select2


class Form1(forms.ModelForm):
    name = forms.CharField(max_length=100, label='name')
    phone = forms.CharField(max_length=100, label='phone')
    place = forms.CharField(max_length=100, label='place')

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'place']
        exclude = ['date_created']


class Form2(forms.ModelForm):
    product_name = forms.CharField(max_length=100, label='product name')
    company_name = forms.CharField(max_length=100, label='company name')
    quantity = forms.FloatField(label='quantity')
    price = forms.FloatField(label='price')

    class Meta:
        model = Stock
        fields = '__all__'
        exclude = ['date_created', 'stock_available']


class Form3(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['total', 'date_created', 'invoice_no']


class Form4(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['place', 'date_created', 'total', 'invoice_no']


class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
