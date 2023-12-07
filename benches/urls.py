from django.urls import path
from . import views

app_name = 'benches'

urlpatterns = [
    path('create_bench/', views.create_bench, name='create_bench'),
    path('', views.bench_list, name='bench_list'),

    
]