# Generated by Django 5.0.3 on 2024-03-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_portfolio_image2_portfolio_image3_portfolio_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='projectUrl',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]