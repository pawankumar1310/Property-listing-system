# Generated by Django 3.2.7 on 2021-10-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0003_auto_20211004_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]