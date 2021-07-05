from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Hiteles email cím megadása.')
    password1 = forms.CharField(
        label=("Jelszó"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=("Jelszava nem lehet túl hasonló a többi személyes adatához. Legalább 8 karakterből kell állnia és nem lehet teljesen numerikus sem."),
    )
    password2 = forms.CharField(
        label=("Jelszó hitelesítés"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Az ellenőrzéshez írja be ugyanazt a jelszót, mint korábban."),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': ('Felhasználónév'),
            'email': ('Email'),
        }
        help_texts = {
            'username': 'Kötelető. Kevesebb, mint 150 karakter. Csak betűk, számjegyek és @ /. / + / - / _.',
        }



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

        labels = {
            'username': ('Felhasználónév'),
            'email': ('Email'),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
