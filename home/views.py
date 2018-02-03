# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def artwork(request):
	return render(request, 'home/artwork.html')

def codework(request):
	return render(request, 'home/codework.html')

def animation(request):
	return render(request, 'home/animation.html')




