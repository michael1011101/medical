# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0006_druginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInfoHelp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manual_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'drug_function_info',
            },
        ),
        migrations.AlterField(
            model_name='druginfo',
            name='telephone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
