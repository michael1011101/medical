# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from bots.base.items import BaseItem
from stalk.models.helpers import DiseaseHelper, SymptomHelper


class DiseaseItem(BaseItem):
    django_model = DiseaseHelper
    update_fields_list = ['name', 'alias', 'link', 'relevant_symptoms']

class SymptomItem(BaseItem):
    django_model = SymptomHelper
    update_fields_list = ['name', 'alias', 'link', 'relevant_diseases']
