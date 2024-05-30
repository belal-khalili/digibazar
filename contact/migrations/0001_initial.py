# Generated by Django 5.0.3 on 2024-05-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('text', models.TextField()),
                ('admin_response', models.TextField()),
            ],
        ),
    ]