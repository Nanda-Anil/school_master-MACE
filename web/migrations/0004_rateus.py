# Generated by Django 4.2 on 2023-05-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rateus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'web_rateus',
                'verbose_name_plural': 'web_rateuss',
            },
        ),
    ]