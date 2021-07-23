# Generated by Django 3.2.5 on 2021-07-23 18:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_customer_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='allergens',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=list, size=None),
        ),
    ]
