# Generated by Django 3.1.7 on 2021-10-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0033_auto_20211030_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores_out',
            name='course_played',
            field=models.CharField(choices=[('BLARNEY', 'BLARNEY'), ('MONSTOWN', 'MONSTOWN')], default='BLARNEY', max_length=15),
        ),
    ]
