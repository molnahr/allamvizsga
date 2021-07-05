from django.db import models
from users.models import Profile
from django.contrib.auth.models import User


class classroom(models.Model):
    classname = models.CharField(max_length=50, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='creator', null=True
    )
    code = models.CharField(max_length=6, null=False, default="passwd")
    user_profile = models.ManyToManyField(Profile)
    image = models.ImageField(null=True,default='default_classroom.jpg', upload_to='classroom_pics')

    def __str__(self):
        return self.classname