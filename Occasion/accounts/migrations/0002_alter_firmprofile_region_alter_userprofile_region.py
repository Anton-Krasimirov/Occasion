# Generated by Django 4.1.3 on 2022-11-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmprofile',
            name='region',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='region',
            field=models.CharField(max_length=30),
        ),
    ]
