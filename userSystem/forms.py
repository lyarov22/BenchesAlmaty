from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Profile

# login system
class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')  # Поля, которые будут отображаться на форме

class LoginForm(AuthenticationForm):
    # Вы можете добавить дополнительные поля, если необходимо
    class Meta:
        model = CustomUser

# profile system
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'bio', 'avatar']
