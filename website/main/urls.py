from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),                                     # https://website/
    path('about', views.about, name='about'),                               # https://website/about
    path('play', views.play, name='play'),                                  # https://website/play
]
