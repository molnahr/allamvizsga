# Generated by Django 3.0 on 2021-06-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='image',
            field=models.ImageField(default='default_classroom.jpg', null=True, upload_to='classroom_pics'),
        ),
    ]
