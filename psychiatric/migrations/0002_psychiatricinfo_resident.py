# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20150916_1053'),
        ('psychiatric', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychiatricinfo',
            name='resident',
            field=models.OneToOneField(related_name='psychiatric_info_table', null=True, to='management.Resident'),
            preserve_default=True,
        ),
    ]