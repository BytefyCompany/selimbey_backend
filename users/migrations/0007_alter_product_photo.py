# Generated by Django 5.0.4 on 2024-05-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_product_subcategory_alter_product_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(max_length=200, null=True, verbose_name='Rasm file_id'),
        ),
    ]