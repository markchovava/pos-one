# Generated by Django 4.2.1 on 2023-07-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0010_alter_sales_options_alter_salesitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='salesitem',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='salesitem',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
