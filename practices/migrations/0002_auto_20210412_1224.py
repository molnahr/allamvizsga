# Generated by Django 2.1.5 on 2021-04-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='level',
            field=models.CharField(choices=[('Kezdő', 'Kezdő'), ('Haladó', 'Haladó'), ('Nehéz', 'Nehéz')], max_length=200, null=True),
        ),
    ]
