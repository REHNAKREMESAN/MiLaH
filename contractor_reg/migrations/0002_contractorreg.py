# Generated by Django 2.0.7 on 2018-11-15 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('security_question', '0002_security_question'),
        ('state', '0002_state'),
        ('district', '0002_district'),
        ('contractor_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractorReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_name', models.CharField(default='', max_length=20)),
                ('house_name', models.CharField(default='', max_length=20)),
                ('street', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('contact', models.BigIntegerField(default='')),
                ('email', models.EmailField(default='', max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('licence', models.BigIntegerField(default='')),
                ('username', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
                ('security_answer', models.CharField(default='', max_length=20)),
                ('status', models.CharField(default='', max_length=20)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.District')),
                ('security_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security_question.Security_question')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.State')),
            ],
        ),
    ]
