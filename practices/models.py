from django.db import models
from django.utils import timezone
from users.models import Profile
from ckeditor.fields import RichTextField

# Command to create migration:
# python manage.py makemigrations (App Name)
# Ex: python manage.py makemigrations MovieReview

# Command to review migration and check database query:
# python manage.py sqlmigrate (App name) (migration file number)
# Ex: python manage.py sqlmigrate MovieReview 0001

# Command to apply migration:
# python manage.py migrate
# Create your models here.

    

class Exercise(models.Model):
    title = models.CharField(max_length=200, null = True)
    LEVEL =(
        ('Könnyű','Könnyű'),
        ('Közepes','Közepes'),
        ('Nehéz','Nehéz')
    )
    level = models.CharField(max_length=200,null = True, choices=LEVEL)
    description = RichTextField(blank=True, null=True)
    EXERCISE_TYPE =(
        ('Verem','Verem'),
        ('Sor','Sor'),
        ('Csatolt Lista','Csatolt Lista'),
        ('Mohó algoritmus','Mohó algoritmus'),
        ('Rekurzió','Rekurzió'),
        ('Dinamikus programozás','Dinamikus programozás'),
        ('Visszalépéses keresés','Visszalépéses keresés'),
        ('Gráfok','Gráfok'),
        ('Bináris keresés', 'Bináris keresés')
    )
    exercise_type = models.CharField(max_length=200,null = True,choices=EXERCISE_TYPE)
    score = models.IntegerField(default=10)
    date_created = models.DateTimeField(default=timezone.now)
    final_answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    
class Solving(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    exercise = models.ManyToManyField(Exercise)
    user_profile = models.ManyToManyField(Profile)
    answer = RichTextField(blank=True, null=True)
    score = models.IntegerField(default=-1)
    comment = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.answer
