from datetime import date
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField("Felhasználónév",max_length=200, null=True)
    email = models.EmailField("E-mail cím",max_length=200, null=True)
    score = models.IntegerField("Pont",null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True,default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


        
# def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 and img.width > 300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)