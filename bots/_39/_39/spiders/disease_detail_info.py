# -*- coding: utf-8 -*-
__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from utils.get_url import get_urls_from_ids
from _39.items import DiseaseDetailInfoItem

class DiseaseDetailInfoSpider(scrapy.Spider):
    name = 'ddi'
    allowed_domains = ['http://jbk.39.net']
    attr = ['jbzs', 'zztz', 'blby', 'yfhl', 'jcjb', 'jb', 'yyzl', 'hl', 'ysbj', 'bfbz']
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id, to_id, *args, **kwargs):
        self.urls = get_urls_from_ids(from_id, to_id, 'disease')
        self.mapping = {}
        super(DiseaseDetailInfoSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for disease_id, url in self.urls.items():
            self.mapping[url] = disease_id
            yield self.make_requests_from_url(url)

    def parse(self, response):
        pass
