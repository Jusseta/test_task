# Generated by Django 5.0 on 2023-12-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(verbose_name='сумма оплаты'),
        ),
    ]
