# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from stalk.models._39 import DiseaseElementaryInfo, DiseaseDetailInfo


class DiseaseElementaryInfoItem(DjangoItem):
    django_model = DiseaseElementaryInfo

class DiseaseDetailInfoItem(DjangoItem):
    django_model = DiseaseDetailInfo

class SymptomInfoItem(DjangoItem):
    pass
