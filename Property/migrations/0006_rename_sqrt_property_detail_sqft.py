# Generated by Django 3.2.7 on 2021-10-10 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0005_property_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_detail',
            old_name='sqrt',
            new_name='sqft',
        ),
    ]
