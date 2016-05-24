# -*- coding: utf-8 -*-
__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from utils.get_url import get_urls_from_ids
from _39.items import DiseaseDetailInfoItem

class DiseaseDetailInfoSpider(scrapy.Spider):
    name = 'ddi'
    allowed_domains = ['http://jbk.39.net']
    url_attr_map = {'jbzs': '疾病简介', 'zztz': '典型症状', 'blby': '发病原因', 'yfhl': '预防', 'jcjb': '临床检查',
                    'jb': '鉴别', 'yyzl': '治疗方法', 'hl': '护理', 'ysbj': '饮食保健', 'bfbz': '并发症'}
    url_attr_db_map = {'jbzs': 'description', 'zztz': 'symptoms', 'blby': 'cause_of_disease',
                        'yfhl': 'prevention', 'jcjb': 'clinical_examination', 'jb': 'distinguish',
                        'yyzl': 'treatment', 'hl': 'nurse', 'ysbj': 'food_conditioning', 'bfbz': 'complication'}
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id, to_id, *args, **kwargs):
        self.urls = get_urls_from_ids(from_id, to_id, 'disease')
        self.mapping = {}
        super(DiseaseDetailInfoSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for disease_id, url in self.urls.items():
            for detail_type in self.url_attr_map.keys():
                self.mapping[url+detail_type] = disease_id
                yield self.make_requests_from_url(url+detail_type)

    def parse(self, response):
        attr_type = response.url.split('/')[-1]
        symbol = (self.mapping.get(response.url), self.url_attr_map[attr_type], response.url)
        self.logger.info('Parsing ID.%d 39health Disease %s Info From <%s>.' % symbol)

        item = DiseaseDetailInfoItem()
        item['d_id'] = symbol[0]
        if attr_type == 'jbzs':
            try:
                item['name'] = get_content(response.xpath('//h1/text()').extract())
                item['description'] = get_content(response.xpath('//div[@class="chi-know"]').extract())
            except:
                pass
        else:
            try:
                item[self.url_attr_db_map[attr_type]] = get_content(response.xpath('//div[@class="art-box"]').extract())
            except:
                pass

        return item
