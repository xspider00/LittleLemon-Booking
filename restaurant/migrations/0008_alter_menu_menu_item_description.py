# Generated by Django 4.1.6 on 2023-02-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_menu_menu_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
