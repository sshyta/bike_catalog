# Generated by Django 5.0 on 2023-12-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='bike_photos/')),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
