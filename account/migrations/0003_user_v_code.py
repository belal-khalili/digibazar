# Generated by Django 5.0.3 on 2024-06-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='v_code',
            field=models.CharField(blank=True, default=False, max_length=5, null=True),
        ),
    ]