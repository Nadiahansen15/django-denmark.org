# Generated by Django 3.2 on 2021-05-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetName', models.CharField(max_length=45)),
                ('houseNumber', models.CharField(max_length=25)),
                ('postalCode', models.CharField(max_length=4)),
                ('region', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='contactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
                ('mainContact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=145)),
                ('description', models.TextField()),
                ('websiteURL', models.CharField(max_length=100)),
                ('relationToDjango', models.TextField()),
                ('compamyAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.address')),
                ('companyContactInformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.contactinformation')),
            ],
        ),
    ]