# Generated by Django 2.0.7 on 2018-11-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chit_details', '0002_chitdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitdetails',
            name='members_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chit_request.ChitRequest'),
        ),
    ]
