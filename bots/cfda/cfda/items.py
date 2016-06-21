# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from bots.base.items import BaseItem
from stalk.models._39 import CFDADrugInfo

class CFDADrug(BaseItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = CFDADrugInfo
    update_fields_list = ['approval_num', 'name', 'en_name', 'trade_name', 'dosage_forms', 'norm',
                          'producer', 'product_address', 'type', 'origin_approval_num', 'approval_date',
                          'drug_based_code', 'remark']
    unique_key = ('url_id',)
