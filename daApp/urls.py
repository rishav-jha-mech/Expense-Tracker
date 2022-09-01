from django.urls import path
from daApp import views

urlpatterns = [
    path('', views.index, name='index'),
]