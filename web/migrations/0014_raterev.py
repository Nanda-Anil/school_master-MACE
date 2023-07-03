# Generated by Django 4.2 on 2023-06-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_delete_rate_us_delete_raterev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raterev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=128, null=True)),
                ('feedback', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'web_rateus',
                'verbose_name_plural': 'web_rateuss',
            },
        ),
    ]
