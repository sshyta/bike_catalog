# Generated by Django 5.0 on 2023-12-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bike',
            options={'ordering': ['-price']},
        ),
        migrations.AlterField(
            model_name='bike',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bike',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bike',
            name='purchase_date',
            field=models.DateField(),
        ),
    ]
