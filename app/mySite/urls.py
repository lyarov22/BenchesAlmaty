from django.urls import path
from . import views

app_name = 'mySite'

urlpatterns = [
    path('map/', views.index, name='index'),
    path('', views.about, name='about'),
]
