from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseNotFound

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


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'shipbattle/login.html', context=context)


def sign_up(request):
    context = {
        'title': 'Sign Up',
    }
    return render(request, 'shipbattle/sign_up.html', context=context)


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


# Error Handlers

def page_not_fount(request, exception):
    return HttpResponseNotFound('404')


def access_denied(request, exception):
    return HttpResponseForbidden('403')


def server_error(request, exception):
    return HttpResponseServerError('500')


# Custom Functions

def mark_active():
    pass
