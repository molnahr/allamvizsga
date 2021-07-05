# Generated by Django 3.0 on 2021-06-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210526_1809'),
        ('practices', '0004_auto_20210526_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='solving',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='solving',
            name='user_profile',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
