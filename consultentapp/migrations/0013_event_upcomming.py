# Generated by Django 5.0 on 2024-01-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultentapp", "0012_event_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="upcomming",
            field=models.BooleanField(default=False),
        ),
    ]
