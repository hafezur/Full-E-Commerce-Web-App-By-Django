# Generated by Django 5.1 on 2024-09-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_orderrequest_is_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=False),
        ),
    ]
