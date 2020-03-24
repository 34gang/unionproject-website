from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('special/', views.special, name="special"),
    path("login/", views.user_login,name="login"),
    path('register/', views.register, name="register_url"),
    path('logout/', views.user_logout, name="logout"),
    path('dashboard/', views.dasbor, name="dasbor"),
]