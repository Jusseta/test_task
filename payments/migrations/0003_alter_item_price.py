# Generated by Django 5.0 on 2023-12-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='сумма оплаты'),
        ),
    ]