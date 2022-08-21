# Generated by Django 4.1 on 2022-08-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=7)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
