# Generated by Django 5.1.4 on 2025-01-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expense", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.FloatField(),
        ),
    ]