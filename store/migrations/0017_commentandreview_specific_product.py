# Generated by Django 5.1 on 2024-10-19 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_commentandreview_avg_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentandreview',
            name='specific_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
