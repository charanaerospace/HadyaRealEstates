# Generated by Django 5.1.3 on 2024-12-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="user_id",
            field=models.IntegerField(blank=True),
        ),
    ]
