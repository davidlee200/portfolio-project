# Generated by Django 3.1.7 on 2021-10-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0031_auto_20211030_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores_out',
            name='hole_10',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_11',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_12',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_13',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='5', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_14',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='5', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_15',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_16',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_17',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_18',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_2',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_3',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_4',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_5',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_6',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_7',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_8',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AddField(
            model_name='scores_out',
            name='hole_9',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
        migrations.AlterField(
            model_name='scores_out',
            name='hole_1',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4', max_length=2),
        ),
    ]
