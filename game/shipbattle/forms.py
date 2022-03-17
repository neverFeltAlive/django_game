from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    """ Represents login form inherited from AuthenticationForm """
    password = forms.CharField(label='Password',
                               strip=False,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control login',
                                   'placeholder': 'CoolPassword123',
                                   'autocomplete': 'current-password',
                               }))
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control login',
                                   'placeholder': 'Gangster123',
                                   'autofocus': True
                               }))
    remember = forms.BooleanField(label='Checkbox',
                                  widget=forms.CheckboxInput(),
                                  required=False)
    field_order = ['username', 'password', 'remember']

    class Meta:
        model = User
        fields = {'username', 'password', 'remember'}


class UserSignUpForm(UserCreationForm):
    """ Represents sign up form inherited from UserCreationForm """
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control signup',
                                   'placeholder': 'Gangster123',
                               }))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control signup',
                                 'placeholder': 'name@example.com',
                             }))
    password1 = forms.CharField(label='Password',
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control signup',
                                    'placeholder': 'CoolPassword123',
                                    'autocomplete': 'new-password',
                                }))
    password2 = forms.CharField(label='Confirm Password',
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control signup',
                                    'placeholder': 'CoolPassword123',
                                    'autocomplete': 'new-password',
                                }))
    agreement = forms.BooleanField(label='Checkbox',
                                   widget=forms.CheckboxInput(),
                                   error_messages={
                                       'required': 'You need to agree to terms of this site'
                                   })
    field_order = ['username', 'email', 'password1', 'password2', 'agreement']

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2', 'agreement'}
