# Generated by Django 3.2.16 on 2022-11-17 00:11

from django.db import migrations
import schoolappi.models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolappi', '0014_alter_student_address_line_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=schoolappi.models.NameField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=schoolappi.models.NameField(max_length=100),
        ),
    ]
