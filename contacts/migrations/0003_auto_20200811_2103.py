# Generated by Django 3.1 on 2020-08-12 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200811_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messages',
            new_name='message',
        ),
    ]
