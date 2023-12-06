from django.shortcuts import render

from userSystem.models import Profile

def index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, "mySite/index.html", {'profile': profile})
    else:
        return render(request, "mySite/index.html")


