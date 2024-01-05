# Generated by Django 5.0 on 2024-01-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultentapp', '0006_alter_consultentprofile_average_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultentprofile',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultentprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consultentprofile',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
