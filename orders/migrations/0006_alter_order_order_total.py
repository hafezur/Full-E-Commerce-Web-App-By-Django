# Generated by Django 5.1 on 2024-08-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_find_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(null=True),
        ),
    ]
