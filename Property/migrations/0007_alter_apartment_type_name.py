# Generated by Django 3.2.7 on 2021-10-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0006_rename_sqrt_property_detail_sqft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment_type',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]