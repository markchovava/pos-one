# Generated by Django 4.2.1 on 2023-07-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0011_alter_currency_created_at_alter_currency_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='ref_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]