# Generated by Django 3.2.16 on 2022-11-17 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolappi', '0024_auto_20221117_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
    ]
