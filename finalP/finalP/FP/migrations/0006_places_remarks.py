# Generated by Django 5.0.3 on 2024-07-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FP', '0005_remove_places_non_operating_places_operating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='remarks',
            field=models.TextField(null=True),
        ),
    ]
