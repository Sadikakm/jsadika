# Generated by Django 3.2.5 on 2021-07-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='Creation',
            new_name='creation',
        ),
    ]