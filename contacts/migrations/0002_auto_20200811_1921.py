# Generated by Django 3.1 on 2020-08-12 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listings',
            new_name='listing',
        ),
    ]
