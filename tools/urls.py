from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="toolsmain"),
    path('ytdownloader/', views.download, name='download')
]