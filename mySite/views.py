from django.shortcuts import get_object_or_404, render, redirect

from userSystem.models import Profile

def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "mySite/index.html", {'profile': profile})


