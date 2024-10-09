from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import CustomUser


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(label='Last Name',
                                required=True,
                                widget=forms.TextInput(attrs={
                                                              'class': 'form-control',
                                                              }))
    
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    # email=forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(
    label='Email',
    required=True,
    widget=forms.EmailInput(attrs={'class':'form-control'}),
    help_text=""
)

    class Meta:
        # model = User
        model =CustomUser

        fields = ['first_name','last_name','username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')

    #     if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
    #         raise ValidationError('Email must have at least 6 alphabets.')        
    #     return email

        
class NewLoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class EditUserForm(NewUserForm):

    class Meta(NewUserForm.Meta):
        model = CustomUser

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A user with that username already exists.')
        return username
