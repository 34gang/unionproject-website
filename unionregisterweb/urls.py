from django.contrib import admin
from django.urls import path, include
from . import views
from accounts import views as accview
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.index, name="utama"),
    path('accounts/', include("accounts.urls")),
    path('bergabung/', accview.index, name="home"),
]
