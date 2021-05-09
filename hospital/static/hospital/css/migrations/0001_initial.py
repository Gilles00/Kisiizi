# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-09 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reception', '__first__'),
        ('operations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('charges', models.CharField(default=0, max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.Patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
