# Generated by Django 3.2.13 on 2022-09-22 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
