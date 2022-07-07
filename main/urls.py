from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ru/', views.index, name='ru')
]
