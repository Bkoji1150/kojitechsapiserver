# Generated by Django 3.2.16 on 2022-11-17 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolappi', '0018_alter_payment_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_user', to='schoolappi.course'),
        ),
    ]