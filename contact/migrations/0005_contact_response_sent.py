# Generated by Django 5.0.3 on 2024-11-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contact_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='response_sent',
            field=models.BooleanField(default=False),
        ),
    ]
