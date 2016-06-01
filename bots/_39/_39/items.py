# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from bots.base.items import BaseItem
from stalk.models._39 import DiseaseElementaryInfo, DiseaseDetailInfo, SymptomDetailInfo


class DiseaseElementaryInfoItem(BaseItem):
    django_model = DiseaseElementaryInfo
    update_fields_list = ['name', 'position', 'medicare', 'department', 'infectiousness', 'infectious_method',
                          'treatment_method', 'treatment_rate', 'major_groups', 'treatment_fee', 'typical_symptoms',
                          'clinical_examination', 'complication', 'surgery', 'relative_drugs']
    unique_key = ('d_id',)

class DiseaseDetailInfoItem(BaseItem):
    django_model = DiseaseDetailInfo
    update_fields_list = ['name', 'description', 'symptoms', 'cause_of_disease', 'prevention', 'clinical_examination',
                          'distinguish', 'treatment', 'nurse', 'food_conditioning', 'complication']
    unique_key = ('d_id',)

class SymptomDetailInfoItem(BaseItem):
    django_model = SymptomDetailInfo
    update_fields_list = ['name', 'description', 'cause_of_symptom', 'diagnostic_details']
    unique_key = ('s_id',)
