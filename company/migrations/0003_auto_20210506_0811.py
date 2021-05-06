# Generated by Django 3.2 on 2021-05-06 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210504_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='houseNumber',
            field=models.IntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='postalCode',
            field=models.IntegerField(max_length=4),
        ),
    ]