from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'artwork/', views.artwork),
    url(r'research/', views.research),
    url(r'animation/', views.animation),
    url(r'resume/', views.resume),
    url(r'about/', views.about),
    url(r'projects/',views.projects),
    url(r'paintings/',views.paintings),
    url(r'webdev/',views.webdev),
    url(r'drawings/',views.drawings),
    url(r'coding/',views.coding),
    url(r'houdini/',views.houdini),
    url(r'redshift/',views.redshift),
]
