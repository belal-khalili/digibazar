# Generated by Django 5.0.3 on 2024-09-09 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='body',
        ),
    ]
