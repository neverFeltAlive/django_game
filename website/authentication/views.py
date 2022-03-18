from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseNotFound, \
    HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import CreateView, FormView, UpdateView, DetailView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.decorators import login_required

from .forms import UserSignUpForm, UserLoginForm, UserEditProfileForm, UserChangePasswordForm
from .utils import AuthenticationUserPassedTestMixin


@login_required(login_url='main:home')
def user_logout(request):
    """ Logs user out and redirects back """
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# region Form Views
class UserPasswordResetView(LoginRequiredMixin, PasswordResetView):
    pass


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserChangePasswordForm
    success_url = reverse_lazy('authentication:login')
    template_name = 'authentication/password_change.html'


class UserEditProfileView(LoginRequiredMixin, UpdateView):
    """ Shows detailed view of a user's profile in a form.
        If the user is not logged in redirects to login page """
    form_class = UserEditProfileForm
    template_name = 'authentication/profile.html'
    success_url = reverse_lazy('authentication:profile')

    def get_object(self):
        return self.request.user


class UserLoginView(AuthenticationUserPassedTestMixin, LoginView):
    """ Logins a user using special form class (UserLoginForm) if form is valid
        fills the form with user input and displays errors otherwise.
        If user is already logged in raises 403 """
    form_class = UserLoginForm
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class UserSignUpView(AuthenticationUserPassedTestMixin, CreateView):
    """ Registers a user using special form class (UserSignUpForm) if form is valid
        fills the form with user input and displays errors otherwise.
        If user is already logged in raises 403 """
    form_class = UserSignUpForm
    template_name = 'authentication/sign_up.html'
    success_url = reverse_lazy('authentication:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated
# endregion
