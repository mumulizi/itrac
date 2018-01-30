# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_problem',
            name='ProblemStatus',
            field=models.CharField(choices=[('yes', '\u4ee5\u89e3\u51b3'), ('no', '\u672a\u89e3\u51b3'), ('wait', '\u5f85\u89e3\u51b3')], default='no', max_length=10, verbose_name='\u662f\u5426\u5b8c\u6210'),
        ),
        migrations.AlterField(
            model_name='add_problem',
            name='ProblemTime',
            field=models.CharField(max_length=40, verbose_name='\u62a5\u4fee\u65f6\u95f4'),
        ),
    ]
