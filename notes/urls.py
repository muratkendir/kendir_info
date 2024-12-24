from django.urls import path

from . import views

urlpatterns = [
    path('', views.allnotes, name='allnotes'),
    path('<int:note_id>', views.detail, name='detail'),
] 
