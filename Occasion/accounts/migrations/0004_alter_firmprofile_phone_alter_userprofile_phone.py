# Generated by Django 4.1.3 on 2022-11-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmprofile',
            name='phone',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]