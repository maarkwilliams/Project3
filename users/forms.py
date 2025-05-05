from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


# Custom form for user creation with email field included
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter your email'}
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


# Form for updating user profile details
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['bio', 'profile_picture']
