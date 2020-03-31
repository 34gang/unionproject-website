from django.urls import path
from . import views

urlpatterns = [
    path('ytdownloader/', views.download, name='download' )
]