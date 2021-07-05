from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#Minden alkalommal, amikor létrehozunk egy Usert hozzuk létreannak a Profilját is.
# Ezt írhatnánk Models.py ba is, de ez a django álltal javasolt.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
        user=instance,
        name=instance.username,
        email=instance.email)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
