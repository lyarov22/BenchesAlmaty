from django.urls import path
from . import views

app_name = 'mySite'

urlpatterns = [
    path('', views.index, name='index'),

    
]