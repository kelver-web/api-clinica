# Generated by Django 4.1 on 2022-08-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=10)),
                ('cep', models.IntegerField()),
                ('social_reason', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Clinica',
                'verbose_name_plural': 'Clinicas',
            },
        ),
    ]
