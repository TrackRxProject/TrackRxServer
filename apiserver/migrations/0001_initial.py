# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adherence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'adherence',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dosage', models.TextField()),
            ],
            options={
                'db_table': 'info',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField()),
                ('interval', models.CharField(max_length=5)),
                ('activate', models.BooleanField()),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
        migrations.AddField(
            model_name='info',
            name='uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiserver.Prescription'),
        ),
        migrations.AddField(
            model_name='adherence',
            name='uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiserver.Prescription'),
        ),
    ]
