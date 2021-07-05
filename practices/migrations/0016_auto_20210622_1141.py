# Generated by Django 3.0 on 2021-06-22 09:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0015_auto_20210621_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_type',
            field=models.CharField(choices=[('Verem', 'Verem'), ('Sor', 'Sor'), ('Csatolt Lista', 'Csatolt Lista'), ('Mohó algoritmus', 'Mohó algoritmus'), ('Rekurzió', 'Rekurzió'), ('Dinamikus programozás', 'Dinamikus programozás'), ('Visszalépéses keresés', 'Visszalépéses keresés'), ('Gráfok', 'Gráfok'), ('Bináris keresés', 'Bináris keresés')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='final_answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solving',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solving',
            name='comment',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
