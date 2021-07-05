from django import forms
from .models import Exercise, Solving


class AddAnswerExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('final_answer',)

        labels = {
            'final_answer': ('Helyes válasz megadása'),
        }

        widgets = {
            'final_answer': forms.Textarea(attrs={'class': 'form-control'}),

        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('title','level','exercise_type','description','score')

        labels = {
            'title': ('Cím'),
            'level': ('Szint'),
            'exercise_type': ('Típus'),
            'description': ('A feladat szövege'),
            'score': ('Pont'),
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'exercise_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-score'}),
        }


class SolveExerciseForm(forms.ModelForm):
    class Meta:
        model = Solving
        fields = ('answer',)

        labels = {
            'answer': ('Megoldás'),
        }

        widgets = {
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddScoreToAnswerTeacherForm(forms.ModelForm):
    class Meta:
        model = Solving
        fields = ('score','comment')

        labels = {
            'comment': ('A megoldásról való vélemény'),
            'score': ('Elért pontszám'),
        }

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-score'}),
        }
