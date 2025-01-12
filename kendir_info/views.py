from django.http import HttpResponse
from django.shortcuts import render
import operator
from jobs.models import Job
from notes.models import Note

def home(request):
	last_jobs = Job.objects.all()[:3]
	last_notes = Note.objects.all()[:3]
	return render(request, 'home.html', {'last_jobs':last_jobs, 'last_notes':last_notes})
