# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listSummary', '0014_auto_20160229_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vino_transfersummary_year',
            old_name='vino_transfersummary_id',
            new_name='vino_transfersummary',
        ),
    ]