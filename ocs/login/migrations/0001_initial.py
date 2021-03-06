# Generated by Django 3.0.1 on 2020-01-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_pnr', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('s_roll', models.IntegerField()),
                ('s_class', models.CharField(max_length=50)),
                ('s_contact', models.IntegerField()),
                ('s_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('t_id', models.IntegerField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=50)),
            ],
        ),
    ]
