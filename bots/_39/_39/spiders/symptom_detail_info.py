# -*- coding: utf-8 -*-
__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from utils.get_url import get_urls_from_ids
from _39.items import SymptomDetailInfoItem

class SymptomDetailInfoSpider(scrapy.Spider):
    name = 'sdi'
    allowed_domains = ['http://jbk.39.net']
    url_attr_map = {'': '综述', 'zzqy': '症状起因', 'zdxs': '诊断详述'}
    url_attr_db_map = {'zzqy': 'cause_of_symptom', 'zdxs': 'diagnostic_details'}
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id, to_id, *args, **kwargs):
        self.urls = get_urls_from_ids(from_id, to_id, 'symptom')
        self.mapping = {}
        super(SymptomDetailInfoSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for symptom_id, url in self.urls.items():
            yield self.make_requests_from_url(url)
            for detail_type in self.url_attr_map.keys():
                self.mapping[url+detail_type] = symptom_id
                yield self.make_requests_from_url(url+detail_type)

    def parse(self, response):
        attr_type = response.url.split('/')[-1]

        symbol = (self.mapping.get(response.url), self.url_attr_map[attr_type], response.url)
        self.logger.info('Parsing ID.%d 39health Symptom %s Info From <%s>.' % symbol)

        item = SymptomDetailInfoItem()
        item['s_id'] = symbol[0]
        if attr_type == '':
            try:
                item['name'] = get_content(response.xpath('//h1/text()').extract())
                item['description'] = get_content(response.xpath('//dd[@id="intro"]/p/text()').extract())
            except:
                pass
        else:
            try:
                item[self.url_attr_db_map[attr_type]] = \
                    get_content(response.xpath('//div[@class="item catalogItem"]').extract())
            except:
                pass

        return item
