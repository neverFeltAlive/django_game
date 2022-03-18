from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
    # https://website/login
    path('logout', views.user_logout, name='logout'),
    # https://website/logout
    path('sign-up', views.UserSignUpView.as_view(), name='sign_up'),
    # https://website/sign-up
    path('profile', views.UserEditProfileView.as_view(), name='profile'),
    # https://website/profile
    path('profile/password-change', views.UserPasswordChangeView.as_view(), name='password_change'),
    # https://website/profile/edit/password
    path('profile/password-reset', views.UserPasswordResetView.as_view(), name='password_reset'),
    # https://website/profile/password-reset
]
