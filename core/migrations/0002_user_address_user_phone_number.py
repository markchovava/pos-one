# Generated by Django 4.2.1 on 2023-07-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
