# Generated by Django 3.0 on 2021-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0009_auto_20210608_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='final_answer',
            field=models.TextField(null=True),
        ),
    ]