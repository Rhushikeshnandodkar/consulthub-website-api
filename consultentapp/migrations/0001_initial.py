# Generated by Django 5.0 on 2023-12-16 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateogry_field', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_field', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_field', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultent_name', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('profile_image', models.ImageField(upload_to='profile-pics')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_meetings', models.IntegerField(blank=True, null=True)),
                ('meetings_cancelled', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.IntegerField(blank=True, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultentapp.categorymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('languages', models.ManyToManyField(to='consultentapp.languagemodel')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultentapp.locationmodel')),
            ],
        ),
    ]
