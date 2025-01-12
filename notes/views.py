from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Note, List, Tag, Relationship

# Create your views here.

def allnotes2(request):
    
    tag = request.GET.get('tag', 'Not provided')
    context = {'notelist': notelist, 'tag':tag, 'type': 'Notes'}
    return render(request, 'note/display.html', context)

def allnotes(request):
	# Get the parameters defined in URL (?list_id=1 or  ?tag_id=3)
	list_id = request.GET.get('list_id', 0)
	tag_id = request.GET.get('tag_id', 0)
	if list_id != 0 and tag_id == 0:
		notes = Note.objects.filter(list_id=int(list_id))
		
	elif list_id == 0 and tag_id != 0:
		related_notes = Relationship.objects.filter(tag=int(tag_id))
		related_notes_ids = related_notes.values_list('note_id', flat=True)
		notes = Note.objects.filter(id__in=related_notes_ids)
		print('here comes the sun')
	else:
		notes = Note.objects
	lists = List.objects
	tags = Tag.objects
	return render(request, 'note/allnotes.html', {'notes':notes, 'lists':lists, 'tags':tags, 'list_id':list_id, 'tag_id':tag_id})

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