from django.shortcuts import render, get_object_or_404

from .models import Note

# Create your views here.
def allnotes(request):
	notes = Note.objects
	return render(request, 'note/allnotes.html', {'notes':notes})

def detail(request, note_id):
	detailnote = get_object_or_404(Note, pk=note_id)
	return render(request, 'note/detail.html', {'note':detailnote})