# Generated by Django 4.1.3 on 2022-11-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolappi", "0007_alter_course_course_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="course", name="avg_rating", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="course",
            name="number_rating",
            field=models.IntegerField(default=0),
        ),
    ]