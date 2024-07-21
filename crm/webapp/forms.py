from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import Record



# Register/Create a user 

class CreateUserForm(UserCreationForm):
    phone_number = forms.IntegerField(widget=forms.NumberInput())
   
    class Meta:
        model = User
        fields = ['username', 'phone_number','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
            }),
            'phone_number': forms.NumberInput(attrs={
                'placeholder': 'Enter your Phone Number',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Enter your password',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirm your password',
            }),
        }

# Login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder':'Enter Username'}), )
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Enter Password'}))



# Create a record

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record 
        fields = ['first_name', 'last_name', 'phone', 'category', 'address', 'tall', 'weight', 'price']  





# Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record 
        fields = ['first_name', 'last_name', 'phone', 'category', 'address', 'tall', 'weight', 'price']  
