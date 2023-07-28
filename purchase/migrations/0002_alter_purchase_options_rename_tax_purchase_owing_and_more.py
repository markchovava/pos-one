# Generated by Django 4.2.1 on 2023-07-27 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['purchase_ref', '-created_at', '-updated_at']},
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='tax',
            new_name='owing',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='grandtotal',
            new_name='purchase_total',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='subtotal',
        ),
    ]