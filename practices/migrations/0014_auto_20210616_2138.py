# Generated by Django 3.0 on 2021-06-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0013_auto_20210616_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solving',
            name='score',
            field=models.IntegerField(default=-1),
        ),
    ]