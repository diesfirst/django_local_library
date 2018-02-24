from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'artwork/', views.artwork),
	url(r'codework/', views.codework),
	url(r'animation/', views.animation),
]
