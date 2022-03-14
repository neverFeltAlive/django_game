from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index')


def login(request):
    return HttpResponse('Login')


def sign_up(request):
    return HttpResponse('Sign Up')


def play(request):
    return HttpResponse('Play')
