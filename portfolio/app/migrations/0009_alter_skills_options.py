# Generated by Django 5.0.3 on 2024-03-26 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_skills_rateskill_1to100_skills_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name_plural': 'Skills'},
        ),
    ]