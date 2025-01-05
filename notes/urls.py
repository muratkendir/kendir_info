from django.urls import path

from . import views

urlpatterns = [
    path('', views.allnotes, name='allnotes'),
    path('<int:note_id>', views.detail, name='detail'),
    path('list/<int:list_id>', views.list_notes, name='list_notes'),
    path('tag/<int:tag_id>', views.tag_notes, name='tag_notes'),
]
