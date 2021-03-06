# Generated by Django 2.0.7 on 2018-11-25 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chit', '0002_chit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChitRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.BigIntegerField()),
                ('chit_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chit.Chit')),
            ],
        ),
    ]
