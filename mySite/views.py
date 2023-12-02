from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from BenchesAlmaty import settings
from .models import Category, Advertisement, Profile, Book
from .forms import RegistrationForm, LoginForm, ProfileForm, AdvertisementForm

default_advertisement_avatar_url = settings.MEDIA_URL + 'book_avatars/default_avatar.png'  # Путь к фотографии по умолчанию
default_user_avatar_url = settings.MEDIA_URL + 'user_avatars/default_avatar.png'  # Путь к фотографии по умолчанию

def index(request):
   
    return render(request, "index.html")


# login system
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входить пользователя после успешной регистрации
            return redirect('reSite:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reSite:index')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('reSite:index')


# profile system
@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не существует, создайте его здесь
        profile = Profile(user=request.user)
        profile.save()
    
    return render(request, 'profile/view_profile.html', {'profile': profile, 'default_avatar_url': default_user_avatar_url})

@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не существует, создайте его здесь
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('reSite:view_profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form, 'profile': profile, 'default_avatar_url': default_user_avatar_url})
