from django.urls import path

from . import views

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),         # https://website/login
    path('logout', views.user_logout, name='logout'),                   # https://website/logout
    path('sign-up', views.UserSignUpView.as_view(), name='sign_up'),    # https://website/sign-up
]
