# Generated by Django 5.1 on 2024-08-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_product_category_order_product_name'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.ManyToManyField(related_name='orders', to='store.product'),
        ),
    ]
