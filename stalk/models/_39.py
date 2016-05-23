from __future__ import unicode_literals

from django.db import models

class DiseaseElementaryInfo(models.Model):
    d_id = models.IntegerField()
    name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=100, null=True)
    medicare = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    infectiousness = models.CharField(max_length=100, null=True)
    infectious_method = models.CharField(max_length=100, null=True)
    treatment_method = models.CharField(max_length=255, null=True)
    treatment_rate = models.CharField(max_length=100, null=True)
    major_groups = models.CharField(max_length=100, null=True)
    treatment_fee = models.CharField(max_length=100, null=True)
    typical_symptoms = models.CharField(max_length=255, null=True)
    clinical_examination = models.CharField(max_length=255, null=True)
    complication = models.CharField(max_length=255, null=True)
    surgery = models.CharField(max_length=255, null=True)
    relative_drugs = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'disease_elementary_info'

class DiseaseDetailInfo(models.Model):
    d_id = models.IntegerField()
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    cause_of_disease = models.TextField(null=True)
    symptoms = models.TextField(null=True)
    food_conditioning = models.TextField(null=True)
    prevention = models.TextField(null=True)
    treatment = models.TextField(null=True)
    examination = models.TextField(null=True)
    complication = models.TextField(null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'disease_detail_info'