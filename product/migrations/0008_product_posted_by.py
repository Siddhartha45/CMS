# Generated by Django 3.1 on 2022-03-24 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_remove_product_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='posted_by',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
    ]
