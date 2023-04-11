# Generated by Django 4.1.7 on 2023-04-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeAds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikename', models.CharField(max_length=50)),
                ('biketype', models.CharField(choices=[('Touring', 'Touring'), ('Sports', 'Sports'), ('Mopads', 'Mopads'), ('Naked', 'Naked')], default='', max_length=50)),
                ('bikediscription', models.TextField()),
                ('bikerentprice', models.FloatField()),
                ('bikebrand', models.CharField(choices=[('KTM', 'KTM'), ('BAJAJ', 'BAJAJ'), ('BMW', 'BMW'), ('TVS', 'TVS'), ('HERO', 'HERO'), ('HONDA', 'HONDA')], default='', max_length=50)),
                ('bikeenginesize', models.IntegerField()),
                ('bikemileage', models.FloatField()),
                ('bikefueltanksize', models.IntegerField()),
                ('bikeweight', models.IntegerField()),
                ('bikewithabs', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=50)),
                ('biketopspeed', models.IntegerField()),
                ('bikeimage', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]