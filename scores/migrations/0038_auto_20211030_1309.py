# Generated by Django 3.1.7 on 2021-10-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0037_auto_20211030_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores_out',
            name='course_played',
            field=models.CharField(max_length=50),
        ),
    ]
