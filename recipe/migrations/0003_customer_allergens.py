# Generated by Django 3.2.5 on 2021-07-23 17:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210722_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='allergens',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=[], size=None),
            preserve_default=False,
        ),
    ]