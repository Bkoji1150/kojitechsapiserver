# Generated by Django 3.2.16 on 2022-11-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolappi', '0028_auto_20221117_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='total_amount_paid',
            field=models.IntegerField(default=0),
        ),
    ]
