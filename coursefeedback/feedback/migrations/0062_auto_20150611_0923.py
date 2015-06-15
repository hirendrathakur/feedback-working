# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0061_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 9, 23, 7, 656428)),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 9, 23, 7, 655818)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 9, 23, 7, 657010)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 9, 23, 7, 653623)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 9, 23, 7, 654544)),
        ),
    ]
