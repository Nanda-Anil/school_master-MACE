# Generated by Django 4.2 on 2023-06-04 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_raterev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raterev',
            old_name='description',
            new_name='feedback',
        ),
    ]
