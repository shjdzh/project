# Generated by Django 3.0.3 on 2020-05-03 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_search_judgement', '0009_auto_20200503_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='judgement_system',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 22, 35, 15, 950391)),
        ),
    ]
