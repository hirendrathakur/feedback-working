# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_1', models.CharField(max_length=1000, null=True, blank=True)),
                ('comment_2', models.CharField(max_length=1000, null=True, blank=True)),
                ('comment_3', models.CharField(max_length=1000, null=True, blank=True)),
                ('comment_4', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prof_date', models.DateTimeField(default=datetime.datetime(2015, 4, 5, 9, 10, 25, 345000))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('done', models.IntegerField(default=0, max_length=1)),
                ('course', models.ForeignKey(to='feedback.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prof_name', models.CharField(max_length=100)),
                ('prof_id', models.CharField(max_length=20)),
                ('prof_date', models.DateTimeField(default=datetime.datetime(2015, 4, 5, 9, 10, 25, 345000))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('question_date', models.DateTimeField(default=datetime.datetime(2015, 4, 5, 9, 10, 25, 355000))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excellent_votes', models.IntegerField(default=0)),
                ('verygood_votes', models.IntegerField(default=0)),
                ('good_votes', models.IntegerField(default=0)),
                ('fair_votes', models.IntegerField(default=0)),
                ('poor_votes', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
                ('course', models.ForeignKey(to='feedback.Course')),
                ('question', models.ForeignKey(to='feedback.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('roll_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('branch', models.CharField(max_length=100)),
                ('semester', models.IntegerField(max_length=2)),
                ('student_date', models.DateTimeField(default=datetime.datetime(2015, 4, 5, 9, 10, 25, 345000))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=10)),
                ('semester', models.IntegerField(max_length=2)),
                ('subject_date', models.DateTimeField(default=datetime.datetime(2015, 4, 5, 9, 10, 25, 345000))),
                ('students', models.ManyToManyField(to='feedback.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='done',
            name='student',
            field=models.ForeignKey(to='feedback.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(to='feedback.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(to='feedback.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(to='feedback.Course'),
            preserve_default=True,
        ),
    ]
