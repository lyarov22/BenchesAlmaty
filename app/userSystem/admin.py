from django.contrib import admin

from userSystem.models import Profile, CustomUser

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass