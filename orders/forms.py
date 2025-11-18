from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','phone','email','address_line1','address_line2','country','state','city','order_note']


from django import forms

class OrderMakeForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address', 'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'})
    )
    product_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter product name', 'class': 'form-control'})
    )
    address_line1 = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Address line1', 'class': 'form-control'})
    )
    address_line2 = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Address line2', 'class': 'form-control'})
    )
    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your city', 'class': 'form-control'})
    )
    state = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your state', 'class': 'form-control'})
    )
    conutry = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your country', 'class': 'form-control'})
    )
    order_note= forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your country', 'class': 'form-control'})
    )
    