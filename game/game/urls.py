"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import handler404, handler403, handler400, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shipbattle.urls'))
]

handler400 = 'shipbattle.views.bad_request'                     # bad request
handler404 = 'shipbattle.views.page_not_fount'                  # page not found
handler403 = 'shipbattle.views.access_denied'                   # access denied
handler500 = 'shipbattle.views.server_error'                    # server error
