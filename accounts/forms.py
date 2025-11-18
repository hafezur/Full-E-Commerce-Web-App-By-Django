from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'form-control',}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    

    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']
        
    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password !=confirm_password:
            raise forms.ValidationError("Password does not match!")

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs) # registration form ar sob kiso access paya gelam
        self.fields['first_name'].widget.attrs['placeholder'] ='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] ='Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] ='Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] ='Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control' # form-control is a bootstrap property, in an every field this is applied.


class ImageUploadForm(forms.Form):
    image = forms.ImageField()    
    

# forms.py
from django import forms
from .models import Account


    

# class ProfileUpdateForm(forms.Form):
#     first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}))
#     last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}))
#     email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address', 'class': 'form-control'}))       
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class': 'form-control'}))       
#     phone_number= forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}))       

from django import forms

class ProfileUpdateForm(forms.Form):
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
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'})
    )


from django import forms

class AddressUpdateForm(forms.Form):
    address_line1 = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Address Line 1', 'class': 'form-control'})
    )
    state = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter State', 'class': 'form-control'})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter City', 'class': 'form-control'})
    )
    country = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Country', 'class': 'form-control'})
    )
