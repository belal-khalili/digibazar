# Generated by Django 5.0.3 on 2024-06-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_subject_alter_contact_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='contact'),
        ),
    ]
