# Generated by Django 5.0.3 on 2024-07-04 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FP', '0003_alter_places_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='state',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='FP.states'),
            preserve_default=False,
        ),
    ]
