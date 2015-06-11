# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20150503_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 6, 43, 34, 662000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 6, 43, 34, 661000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 6, 43, 34, 664000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 6, 43, 34, 658000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 6, 43, 34, 659000)),
            preserve_default=True,
        ),
    ]
