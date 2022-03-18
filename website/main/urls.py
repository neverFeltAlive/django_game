from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),                                     # https://website/
    path('about', views.about, name='about'),                               # https://website/about
    path('play', views.play, name='play'),                                  # https://website/play
]
