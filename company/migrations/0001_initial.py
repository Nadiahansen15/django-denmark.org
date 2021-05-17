# Generated by Django 3.2 on 2021-05-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=145)),
                ('streetName', models.CharField(default='boooooo', max_length=45)),
                ('houseNumber', models.CharField(default='boooooo', max_length=25)),
                ('postalCode', models.CharField(default='booo', max_length=4)),
                ('region', models.CharField(default='boooooo', max_length=45)),
                ('description', models.TextField()),
                ('phoneNumber', models.CharField(default='boooooo', max_length=11)),
                ('email', models.CharField(default='boooooo', max_length=100)),
                ('mainContact', models.CharField(default='boooooo', max_length=50)),
                ('websiteURL', models.CharField(default='boooooo', max_length=100)),
                ('relationToDjango', models.TextField()),
            ],
        ),
    ]
