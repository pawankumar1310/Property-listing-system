# Generated by Django 3.2.7 on 2021-10-04 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
        migrations.RenameModel(
            old_name='Property_Details',
            new_name='Property_Detail',
        ),
    ]
