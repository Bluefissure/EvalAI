# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-24 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_changed_phase_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='evaluation_script',
            field=models.FileField(default=False, upload_to='evaluationScripts'),
        ),
        migrations.AlterField(
            model_name='testenvironment',
            name='test_annotation',
            field=models.FileField(upload_to='testAnnotations'),
        ),
    ]
