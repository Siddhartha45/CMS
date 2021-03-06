# Generated by Django 3.1 on 2022-04-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_clothes_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='clothes_type',
            field=models.CharField(blank=True, choices=[('MW', 'Male Wear'), ('FW', 'Female Wear')], max_length=12),
        ),
    ]
