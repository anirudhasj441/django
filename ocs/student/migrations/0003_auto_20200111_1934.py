# Generated by Django 3.0.1 on 2020-01-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200111_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigments',
            name='date',
            field=models.DateField(),
        ),
    ]
