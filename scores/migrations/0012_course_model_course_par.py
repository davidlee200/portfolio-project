# Generated by Django 3.1.7 on 2021-04-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0011_auto_20210416_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_model',
            name='Course_Par',
            field=models.IntegerField(default=70),
        ),
    ]
