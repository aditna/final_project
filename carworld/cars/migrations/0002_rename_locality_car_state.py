# Generated by Django 3.2.7 on 2021-10-01 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='locality',
            new_name='state',
        ),
    ]
