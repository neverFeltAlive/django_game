from django import forms
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm


class UserChangePasswordForm(PasswordChangeForm):
    """ Represents password changing form inherited from PasswordChangeForm """
    old_password = forms.CharField(label='Old Password',
                                   strip=False,
                                   widget=forms.PasswordInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'strong password',
                                       'autocomplete': 'current-password',
                                   }))
    new_password1 = forms.CharField(label='Password',
                                    strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'strong password',
                                        'autocomplete': 'new-password',
                                    }))
    new_password2 = forms.CharField(label='Confirm Password',
                                    strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'strong password',
                                        'autocomplete': 'new-password',
                                    }))


class UserEditProfileForm(UserChangeForm):
    """ Represents profile editing form inherited from UserChangeForm """
    username = forms.CharField(label='Username',
                               required=False,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control signup',
                               }))
    first_name = forms.CharField(label='First Name',
                                 required=False,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control signup',
                                 }))
    last_name = forms.CharField(label='Last Name',
                                required=False,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control signup',
                                }))
    email = forms.EmailField(label='Email',
                             required=False,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control signup',
                             }))
    password = None
    field_order = ['first_name', 'last_name', 'username']

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email'}


class UserLoginForm(AuthenticationForm):
    """ Represents login form inherited from AuthenticationForm """
    password = forms.CharField(label='Password',
                               strip=False,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control login',
                                   'placeholder': 'strong password',
                                   'autocomplete': 'current-password',
                               }))
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control login',
                                   'placeholder': 'username',
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
                                   'placeholder': 'username',
                               }))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control signup',
                                 'placeholder': 'username@smth.com',
                             }))
    password1 = forms.CharField(label='Password',
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control signup',
                                    'placeholder': 'strong password',
                                    'autocomplete': 'new-password',
                                }))
    password2 = forms.CharField(label='Confirm Password',
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control signup',
                                    'placeholder': 'strong password',
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
