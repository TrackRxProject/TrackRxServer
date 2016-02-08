# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField()),
            ],
            options={
                'db_table': 'dose',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField()),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField()),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Patient')),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
        migrations.AddField(
            model_name='dose',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Prescription'),
        ),
    ]