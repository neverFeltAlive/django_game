from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                 # https://website/
    path('login', views.login, name='login'),           # https://website/login
    path('sign-up', views.sign_up, name='sign_up'),     # https://website/sign-up
    path('play', views.play, name='play'),              # https://website/play
    path('about', views.about, name='about'),              # https://website/about
]

handler404 = views.page_not_fount               # page not found

# TODO: create server error handlers
'''
handler400                                      # unable to process request
handler403 = views.access_denied                # access denied
handler500 = views.server_error                 # server error
'''
