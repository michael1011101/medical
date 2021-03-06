# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0005_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('category_list', models.CharField(max_length=255, null=True)),
                ('category_first', models.CharField(max_length=255, null=True)),
                ('category_second', models.CharField(max_length=255, null=True)),
                ('cites', models.CharField(max_length=255, null=True)),
                ('english_name', models.CharField(max_length=255, null=True)),
                ('company', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('drug_components', models.TextField(null=True)),
                ('major_function', models.TextField(null=True)),
                ('indication', models.TextField(null=True)),
                ('usages', models.TextField(null=True)),
                ('untoward_reaction', models.TextField(null=True)),
                ('contradication', models.TextField(null=True)),
                ('info', models.TextField(null=True)),
                ('special_crowd_medications', models.TextField(null=True)),
                ('properties', models.TextField(null=True)),
                ('store', models.TextField(null=True)),
                ('validity', models.TextField(null=True)),
                ('approval_num', models.TextField(null=True)),
                ('manual_revision_date', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': '39_drug_function_info',
            },
        ),
    ]
