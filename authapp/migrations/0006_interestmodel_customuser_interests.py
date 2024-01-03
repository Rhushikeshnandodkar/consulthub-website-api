# Generated by Django 5.0 on 2024-01-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='interests',
            field=models.ManyToManyField(to='authapp.interestmodel'),
        ),
    ]
