from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='home'),                                 # https://website/chat
    path('<str:room_name>/', views.room, name='room')                    # https://website/chat/<room_name>
]
