from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'reSite'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/reread-logo.ico', permanent=True), name='favicon'),
    path('', views.index, name='index'),

    # login system
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # profile system
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
]