# Generated by Django 5.0.3 on 2024-06-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]