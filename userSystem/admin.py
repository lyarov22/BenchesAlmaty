from django.contrib import admin

from userSystem.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass