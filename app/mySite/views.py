from django.shortcuts import render

from benches.models import Bench
from userSystem.models import Profile


def index(request):
    benches = Bench.objects.all()

    if request.user.is_authenticated:
        # TODO: исправить костыль с отображением фото, сделать проверку в шаблоне
        profile, created = Profile.objects.get_or_create(user=request.user)
        context = {'profile': profile, 'benches': benches}
    else:
        context = {'benches': benches}

    return render(request, "mySite/index.html", context)

def about(request):
    return render(request, "mySite/about.html")