# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20150405_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 47, 51, 279784)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 47, 51, 279293)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 47, 51, 280248)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 47, 51, 277376)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 47, 51, 278051)),
            preserve_default=True,
        ),
    ]
