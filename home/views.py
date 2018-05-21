# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper

# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def artwork(request):
	return render(request, 'home/artwork/artwork.html')

def research(request):
	return render(request, 'home/projects/research.html')

def animation(request):
	return render(request, 'home/animation.html')

def about(request):
        return render(request, 'home/about.html')

def resume(request):
        path = 'media/Michael_Buckley_Resume.pdf'
        file = open(path, "rb")
        file.seek(0)
        pdf = file.read()
        file.close
        return HttpResponse(pdf, content_type='application/pdf')

def projects(request):
        return render(request, 'home/projects/projects.html')

def paintings(request):
        return render(request, 'home/artwork/paintings.html')

def webdev(request):
        return render(request, 'home/resources/webdev.html')

def drawings(request):
        return render(request, 'home/artwork/drawings.html')

        




