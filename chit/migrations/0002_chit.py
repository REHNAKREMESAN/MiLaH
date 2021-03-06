# Generated by Django 2.0.7 on 2018-10-22 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chit_amount', models.CharField(default='', max_length=10)),
                ('chit_start_date', models.DateField(default=datetime.date.today)),
                ('chit_name', models.CharField(default='', max_length=20)),
                ('login_id', models.BigIntegerField()),
            ],
        ),
    ]
