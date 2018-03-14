# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper

# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def artwork(request):
	return render(request, 'home/artwork.html')

def codework(request):
	return render(request, 'home/codework.html')

def animation(request):
	return render(request, 'home/animation.html')

def resume(request):
        path = 'media/Michael_Buckley_Resume.pdf'
        file = open(path, "rb")
        file.seek(0)
        pdf = file.read()
        file.close
        return HttpResponse(pdf, content_type='application/pdf')

        




