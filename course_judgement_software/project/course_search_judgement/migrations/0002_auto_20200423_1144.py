# Generated by Django 3.0.3 on 2020-04-23 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_search_judgement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgement_system',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 11, 44, 1, 396918)),
        ),
    ]