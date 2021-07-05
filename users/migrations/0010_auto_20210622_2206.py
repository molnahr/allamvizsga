# Generated by Django 3.0 on 2021-06-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210526_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name='E-mail cím'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Felhasználónév'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0, null=True, verbose_name='Pont'),
        ),
    ]
