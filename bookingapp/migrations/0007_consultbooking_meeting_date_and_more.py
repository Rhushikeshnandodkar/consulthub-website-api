# Generated by Django 5.0.6 on 2024-06-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_consultbooking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultbooking',
            name='meeting_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultbooking',
            name='meeting_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultbooking',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
    ]