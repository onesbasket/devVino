# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listSummary', '0015_auto_20160229_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='testVinoGrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grape', models.IntegerField(db_column=b'grape', null=True)),
            ],
            options={
                'db_table': 'testVinoGrape',
            },
        ),
        migrations.AddField(
            model_name='vino_transfersummary',
            name='testmany',
            field=models.ManyToManyField(to='listSummary.testVinoGrape'),
        ),
    ]
