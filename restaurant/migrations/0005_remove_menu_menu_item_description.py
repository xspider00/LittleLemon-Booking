# Generated by Django 4.1.3 on 2023-02-19 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_menu_menu_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
    ]
