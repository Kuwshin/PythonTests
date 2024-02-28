# Generated by Django 5.0.2 on 2024-02-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCar', models.CharField(max_length=255)),
                ('content', models.TextField(default='')),
                ('price', models.PositiveSmallIntegerField(default=1)),
                ('year', models.PositiveSmallIntegerField(default=1800)),
                ('imgCar', models.ImageField(blank=True, null=True, upload_to='mediacar')),
            ],
        ),
    ]
