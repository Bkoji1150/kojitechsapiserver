# Generated by Django 4.1.3 on 2022-11-14 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schoolappi", "0008_course_avg_rating_course_number_rating"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course", old_name="number_rating", new_name="number_of_rating",
        ),
    ]
