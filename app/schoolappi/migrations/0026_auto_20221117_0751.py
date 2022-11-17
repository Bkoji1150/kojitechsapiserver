# Generated by Django 3.2.16 on 2022-11-17 07:51

from django.db import migrations, models
import django.utils.timezone
import schoolappi.models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolappi', '0025_remove_review_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='created',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='payment',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to=schoolappi.models.upload_to),
        ),
    ]
