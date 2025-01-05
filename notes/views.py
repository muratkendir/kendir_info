from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Note, List, Tag, Relationship

# Create your views here.
def allnotes(request):
	notes = Note.objects
	lists = List.objects
	tags = Tag.objects
	return render(request, 'note/allnotes.html', {'notes':notes, 'lists':lists, 'tags':tags})

def list_notes(request, list_id):
	notes = Note.objects.filter(list_id=list_id)
	lists = List.objects
	tags = Tag.objects
	return render(request, 'note/list_notes.html', {'notes':notes, 'lists':lists, 'tags':tags})

def tag_notes(request, tag_id):
	related_notes = Relationship.objects.filter(tag=tag_id)
	related_notes_ids = related_notes.values_list('note_id', flat=True)
	notes = Note.objects.filter(id__in=related_notes_ids)
	lists = List.objects
	tags = Tag.objects
	return render(request, 'note/tag_notes.html', {'notes':notes, 'lists':lists, 'tags':tags})

def detail(request, note_id):
	detailnote = get_object_or_404(Note, pk=note_id)
	return render(request, 'note/detail.html', {'note':detailnote})