# Generated by Django 4.2 on 2024-01-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eMarks',
            field=models.IntegerField(default=0),
        ),
    ]
