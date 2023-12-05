from django.shortcuts import get_object_or_404, render, redirect

from userSystem.models import Profile

def index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, "mySite/index.html", {'profile': profile})
    else:
        return render(request, "mySite/index.html",)


