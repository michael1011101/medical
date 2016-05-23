from __future__ import unicode_literals

from django.db import models
from lolly import Lolly

class DiseaseHelper(Lolly):
    name = models.CharField(max_length=100, null=True)
    alias = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=100, null=True)
    relevant_symptoms = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'disease_helper'

class SymptomHelper(Lolly):
    name = models.CharField(max_length=100, null=True)
    alias = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=100, null=True)
    relevant_diseases = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'symptom_helper'