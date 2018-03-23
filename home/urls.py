from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'artwork/', views.artwork),
    url(r'research/', views.research),
    url(r'animation/', views.animation),
    url(r'resume/', views.resume),
    url(r'about/', views.about),
]
