# Generated by Django 3.1.7 on 2021-05-16 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0016_auto_20210516_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores_out',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]