from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

from BenchesAlmaty import settings
from .models import Profile

from .forms import RegistrationForm, LoginForm, ProfileForm

# login system
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входить пользователя после успешной регистрации
            return redirect('mySite:index')
    else:
        form = RegistrationForm()
    return render(request, 'userSystem/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mySite:index')

    else:
        form = LoginForm()
    return render(request, 'userSystem/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('mySite:index')


# profile system
@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не существует, создайте его здесь
        profile = Profile(user=request.user)
        profile.save()
    
    return render(request, 'userSystem/view_profile.html', {'profile': profile})

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
            if request.POST.get('delete_avatar'):
                profile.avatar = None
                os.remove(profile.get_avatar_url())
                profile.save()
            return redirect('view_profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'userSystem/edit_profile.html', {'form': form, 'profile': profile})
