# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listSummary', '0010_auto_20160222_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='vino_transferSummary_Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summaryId', models.IntegerField(db_column=b'summaryId', null=True)),
                ('year', models.IntegerField(db_column=b'years', null=True)),
            ],
            options={
                'db_table': 'vino_transferSummary_Year',
            },
        ),
    ]
