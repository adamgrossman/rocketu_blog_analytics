# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='date',
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='ip_address',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='view',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='location',
            field=models.ForeignKey(related_name=b'view', blank=True, to='analytics.Location', null=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('city', 'country', 'region')]),
        ),
    ]
