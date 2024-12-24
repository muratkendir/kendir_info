from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'jobs/home.html')

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