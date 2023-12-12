from django.shortcuts import render
from benches.models import Bench

from userSystem.models import Profile

def index(request):
    benches = Bench.objects.all()

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            # Если профиль не существует, создайте его здесь
            profile = Profile(user=request.user)
            profile.save()
        profile = Profile.objects.get(user=request.user)
        return render(request, "mySite/index.html", {'profile': profile, 'benches': benches})
    else:
        return render(request, "mySite/index.html", {'benches': benches})


# ПОФИКСИТЬ КОСТЫЛЬ С ОТОБРАЖЕНИЕМ ФОТО, СДЕЛАТЬ ПРОВЕРКУ В ШАБЛОНЕ