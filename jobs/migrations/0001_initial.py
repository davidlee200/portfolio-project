# Generated by Django 2.0.2 on 2021-03-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgane', models.ImageField(upload_to='image/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
