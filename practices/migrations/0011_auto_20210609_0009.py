# Generated by Django 3.0 on 2021-06-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0010_exercise_final_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solving',
            name='exercise',
            field=models.ManyToManyField(to='practices.Exercise'),
        ),
    ]
