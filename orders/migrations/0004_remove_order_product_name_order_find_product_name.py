# Generated by Django 5.1 on 2024-08-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_product_category_and_more'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='find_product_name',
            field=models.ManyToManyField(to='store.product'),
        ),
    ]
