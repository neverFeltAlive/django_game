from django.urls import path
from django.conf.urls import handler404, handler403, handler400, handler500

from . import views

urlpatterns = [
    path('', views.index, name='home'),                                     # https://website/
    path('login', views.UserLoginView.as_view(), name='login'),             # https://website/login
    path('logout', views.user_logout, name='logout'),                       # https://website/logout
    path('sign-up', views.UserSignUpView.as_view(), name='sign_up'),        # https://website/sign-up
    path('play', views.play, name='play'),                                  # https://website/play
    path('about', views.about, name='about'),                               # https://website/about
]

