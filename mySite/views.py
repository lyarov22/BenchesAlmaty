from django.shortcuts import render

from userSystem.models import Profile

def index(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            # Если профиль не существует, создайте его здесь
            profile = Profile(user=request.user)
            profile.save()
        profile = Profile.objects.get(user=request.user)
        return render(request, "mySite/index.html", {'profile': profile})
    else:
        return render(request, "mySite/index.html")


# ПОФИКСИТЬ КОСТЫЛЬ С ОТОБРАЖЕНИЕМ ФОТО, СДЕЛАТЬ ПРОВЕРКУ В ШАБЛОНЕ