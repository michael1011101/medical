# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-23 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('cause_of_disease', models.TextField(null=True)),
                ('symptoms', models.TextField(null=True)),
                ('food_conditioning', models.TextField(null=True)),
                ('prevention', models.TextField(null=True)),
                ('treatment', models.TextField(null=True)),
                ('examination', models.TextField(null=True)),
                ('complication', models.TextField(null=True)),
            ],
            options={
                'db_table': 'disease_detail_info',
            },
        ),
        migrations.CreateModel(
            name='DiseaseElementaryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('medicare', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('infectiousness', models.CharField(max_length=100, null=True)),
                ('infectious_method', models.CharField(max_length=100, null=True)),
                ('treatment_method', models.CharField(max_length=255, null=True)),
                ('treatment_rate', models.CharField(max_length=100, null=True)),
                ('major_groups', models.CharField(max_length=100, null=True)),
                ('treatment_fee', models.CharField(max_length=100, null=True)),
                ('typical_symptoms', models.CharField(max_length=255, null=True)),
                ('clinical_examination', models.CharField(max_length=255, null=True)),
                ('complication', models.CharField(max_length=255, null=True)),
                ('surgery', models.CharField(max_length=255, null=True)),
                ('relative_drugs', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'disease_elementary_info',
            },
        ),
        migrations.CreateModel(
            name='DiseaseHelper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('relevant_symptoms', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'disease_helper',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=40)),
                ('project', models.CharField(max_length=20, null=True)),
                ('spider', models.CharField(max_length=20, null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='SymptomHelper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('relevant_diseases', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'symptom_helper',
            },
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('job_id', 'project', 'spider')]),
        ),
    ]
