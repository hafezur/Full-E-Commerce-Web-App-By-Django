# Generated by Django 5.1 on 2024-10-19 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_commentandreview_specific_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentandreview',
            name='specific_product',
        ),
        migrations.AddField(
            model_name='product',
            name='specific_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.commentandreview'),
        ),
    ]
