# Generated by Django 5.1 on 2024-09-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_product_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_quentity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('aspected_date', models.DateField()),
            ],
        ),
    ]
