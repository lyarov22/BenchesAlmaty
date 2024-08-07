from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser, Profile


# login system
class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')  # Поля, которые будут отображаться на форме


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Указываем все поля модели, если необходимо


# profile system
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'bio', 'avatar']
