# Generated by Django 3.0.1 on 2020-01-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('s_pnr', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('s_class', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('att_per', models.FloatField()),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
    ]
