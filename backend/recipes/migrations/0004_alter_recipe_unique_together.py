# Generated by Django 4.2.7 on 2023-12-09 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_text'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together=set(),
        ),
    ]
