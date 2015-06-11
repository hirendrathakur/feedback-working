# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0011_auto_20150504_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 17, 0, 1, 518000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 17, 0, 1, 516000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 17, 0, 1, 519000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 17, 0, 1, 512000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 17, 0, 1, 513000)),
            preserve_default=True,
        ),
    ]
