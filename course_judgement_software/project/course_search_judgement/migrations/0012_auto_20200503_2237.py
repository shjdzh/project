# Generated by Django 3.0.3 on 2020-05-03 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_search_judgement', '0011_auto_20200503_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgement_system',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 22, 37, 29, 170421)),
        ),
    ]
