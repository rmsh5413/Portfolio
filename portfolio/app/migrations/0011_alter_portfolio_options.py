# Generated by Django 5.0.3 on 2024-03-26 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_skills_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['id']},
        ),
    ]
