# Generated by Django 5.0.6 on 2024-05-29 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu_item',
            new_name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
