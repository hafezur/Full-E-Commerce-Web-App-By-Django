# Generated by Django 5.1 on 2024-09-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_capacity',
            field=models.IntegerField(default=100),
        ),
    ]