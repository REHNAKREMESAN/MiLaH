# Generated by Django 2.0.7 on 2018-11-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chit_final_install', '0002_chitfinalinstallment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitfinalinstallment',
            name='fmember_name',
            field=models.BigIntegerField(),
        ),
    ]
