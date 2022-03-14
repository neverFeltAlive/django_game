from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                 # https://website/
    path('login', views.login, name='login'),           # https://website/login
    path('sign-up', views.sign_up, name='sign_up'),     # https://website/sign-up
    path('play', views.play, name='play'),              # https://website/play
]
