from django import forms
from .models import classroom

class Join(forms.Form):
    join = forms.CharField(
        strip=True, max_length=6,
        required=True, label="Csatlakozás"
    )

    class Meta:
        model = classroom
        fields = [
            'join'
        ]