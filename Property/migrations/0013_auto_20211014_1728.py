# Generated by Django 3.2.7 on 2021-10-14 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0012_alter_favourite_property_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteProperty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='receive_notification',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Favourite_Property',
        ),
        migrations.AddField(
            model_name='favouriteproperty',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favouriteproperty',
            name='property',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_property', to='Property.Property_Detail'),
        ),
    ]
