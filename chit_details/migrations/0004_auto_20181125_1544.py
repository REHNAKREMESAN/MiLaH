# Generated by Django 2.0.7 on 2018-11-25 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chit_details', '0003_auto_20181125_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chitdetails',
            old_name='members_name',
            new_name='login_id',
        ),
    ]
