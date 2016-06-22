from __future__ import unicode_literals

from django.db import models
from lolly import Lolly
from helpers import NewsHelper

class DiseaseElementaryInfo(Lolly):
    d_id = models.IntegerField(unique=True)
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

class DiseaseDetailInfo(Lolly):
    d_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    symptoms = models.TextField(null=True)
    cause_of_disease = models.TextField(null=True)
    prevention = models.TextField(null=True)
    clinical_examination = models.TextField(null=True)
    distinguish = models.TextField(null=True)
    treatment = models.TextField(null=True)
    nurse = models.TextField(null=True)
    food_conditioning = models.TextField(null=True)
    complication = models.TextField(null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'disease_detail_info'

class SymptomDetailInfo(Lolly):
    s_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    cause_of_symptom = models.TextField(null=True)
    diagnostic_details = models.TextField(null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'symptom_detail_info'

class CFDADrugInfo(Lolly):
    url_id = models.IntegerField(unique=True)
    approval_num = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    en_name = models.CharField(max_length=255, null=True)
    trade_name = models.CharField(max_length=255, null=True)
    dosage_forms = models.CharField(max_length=255, null=True)
    norm = models.CharField(max_length=255, null=True)
    producer = models.CharField(max_length=255, null=True)
    product_address = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    origin_approval_num = models.CharField(max_length=255, null=True)
    approval_date = models.CharField(max_length=255, null=True)
    drug_based_code = models.CharField(max_length=255, null=True)
    remark = models.TextField(null=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'cfda_drug_info'

class News(Lolly):
    newshelper = models.OneToOneField('NewsHelper', to_field='id', db_column='id', primary_key=True)
    title = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=50, null=True)
    source_website = models.CharField(max_length=200, null=True)
    source_website_link = models.CharField(max_length=200, null=True)
    source_author = models.CharField(max_length=200, null=True)
    summary = models.TextField(null=True)
    content = models.TextField(null=True)

    class Meta:
        app_label = 'stalk'
        db_table = '39_news'

class DrugInfo(Lolly):
    manual_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    category_list = models.CharField(max_length=255, null=True)
    cites = models.CharField(max_length=255, null=True)
    english_name = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=50, null=True)
    drug_components = models.TextField(null=True)
    major_function = models.TextField(null=True)
    indication = models.TextField(null=True)
    usages = models.TextField(null=True)
    untoward_reaction = models.TextField(null=True)
    contradication = models.TextField(null=True)
    info = models.TextField(null=True)
    special_crowd_medications = models.TextField(null=True)
    properties = models.TextField(null=True)
    store = models.TextField(null=True)
    validity = models.TextField(null=True)
    approval_num = models.TextField(null=True)
    manual_revision_date = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'stalk'
        db_table = '39_drug_function_info'

class DrugInfoHelp(Lolly):
    manual_id = models.IntegerField(unique=True)

    class Meta:
        app_label = 'stalk'
        db_table = 'drug_function_info'