# Generated by Django 5.1 on 2024-08-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(null=True),
        ),
    ]
