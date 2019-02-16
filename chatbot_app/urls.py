from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	url(r'^get_reply$', views.get_reply, name='get_reply'),   
]
