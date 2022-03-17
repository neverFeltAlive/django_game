from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseNotFound, \
    HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from shipbattle.forms import UserSignUpForm, UserLoginForm
from shipbattle.utils import AuthenticationUserPassedTestMixin

menu = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'About', 'url': 'about'},
    {'name': 'Play', 'url': 'play'},
]


def index(request):
    context = {
        'title': 'Home',
        'menu': menu,
        'active_link': 'Home',
    }
    return render(request, 'shipbattle/index.html', context=context)


@login_required
def play(request):
    context = {
        'title': 'Play',
        'menu': menu,
        'active_link': 'Play',
    }
    return render(request, 'shipbattle/play.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu,
        'active_link': 'About',
    }
    return render(request, 'shipbattle/about.html', context=context)


@login_required(login_url='home')
def user_logout(request):
    """ Logs user out and redirects back """
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# region Error Handlers
def bad_request(request, exception):
    context = {
        'title': '400',
        'error_code': '400',
        'header': 'Incorrect Request',
        'text': 'We are deeply sorry, but the server is unable to process your request correctly. ' +
                'Contact support for more information'
    }
    return render(request, 'shipbattle/server_errors.html', context=context)


def page_not_fount(request, exception):
    context = {
        'title': '404',
        'error_code': '404',
        'header': 'Page Not Found',
        'text': 'Unfortunately, we could not find the page you are looking for. ' +
                'Contact support for more information'
    }
    return render(request, 'shipbattle/server_errors.html', context=context)


def access_denied(request, exception):
    context = {
        'title': '403',
        'error_code': '403',
        'header': 'Access Denied',
        'text': 'We are deeply sorry, but you have no access to this page. ' +
                'Contact support for more information'
    }
    return render(request, 'shipbattle/server_errors.html', context=context)


def server_error(request):
    context = {
        'title': '500',
        'error_code': '500',
        'header': 'Server Error',
        'text': 'We are deeply sorry, but the server ran into some issues processing your request. ' +
                'Contact support for more information'
    }
    return render(request, 'shipbattle/server_errors.html', context=context)
# endregion


# region Form Views
class UserLoginView(AuthenticationUserPassedTestMixin, LoginView):
    """ Logins a user using special form class (UserLoginForm) if form is valid
        fills the form with user input and displays errors otherwise.
        If user is already logged in raises 403 """
    form_class = UserLoginForm
    template_name = 'shipbattle/login.html'


class UserSignUpView(AuthenticationUserPassedTestMixin, CreateView):
    """ Registers a user using special form class (UserSignUpForm) if form is valid
        fills the form with user input and displays errors otherwise.
        If user is already logged in raises 403 """
    form_class = UserSignUpForm
    template_name = 'shipbattle/sign_up.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context

    def test_func(self):
        return not self.request.user.is_authenticated
# endregion
