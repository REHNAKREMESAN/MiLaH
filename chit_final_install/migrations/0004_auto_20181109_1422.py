# Generated by Django 2.0.7 on 2018-11-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chit_final_install', '0003_auto_20181109_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitfinalinstallment',
            name='fmember_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chit_details.ChitDetails'),
        ),
    ]
