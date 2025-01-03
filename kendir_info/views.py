from django.http import HttpResponse
from django.shortcuts import render
import operator
from jobs.models import Job
from notes.models import Note

def home(request):
	last_jobs = Job.objects.all()[:3]
	last_notes = Note.objects.all()[:3]
	return render(request, 'home.html', {'last_jobs':last_jobs, 'last_notes':last_notes})

def count(request):
	ft = request.GET['fulltext']

	wordslist = ft.split()

	worddict = {}

	for word in wordslist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1

	sortedWords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext': ft, 'count': len(wordslist), 'dict': sortedWords})