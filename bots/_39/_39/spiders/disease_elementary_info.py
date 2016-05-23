# -*- coding: utf-8 -*-
__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from utils.get_url import get_urls_from_ids
from _39.items import DiseaseElementaryInfoItem

class DiseaseElementaryInfoSpider(scrapy.Spider):
    name = 'dei'
    allowed_domains = ['http://jbk.39.net']
    d_map = {u'是否属于医保：': 'medicare', u'发病部位：': 'position', u'挂号的科室：': 'department', u'传染性：': 'infectiousness',
             u'传播途径：': 'infectious_method', u'治疗方法：': 'treatment_method', u'治疗率：': 'treatment_rate',
             u'多发人群：': 'major_groups', u'治疗费用：': 'treatment_fee', u'典型症状：': 'typical_symptoms',
             u'并发症：': 'complication', u'临床检查：': 'clinical_examination', u'手术：': 'surgery', u'常用药品：': 'relative_drugs'}
    type_map = {u'是否属于医保：': 1, u'发病部位：': 1, u'挂号的科室：': 1, u'传染性：': 0,
                u'传播途径：': 1, u'治疗方法：': 1, u'治疗率：': 0,
                u'多发人群：': 0, u'治疗费用：': 0, u'典型症状：': 1,
                u'并发症：': 1, u'临床检查：': 1, u'手术：': 1, u'常用药品：': 1}

    def __init__(self, from_id, to_id, *args, **kwargs):
        self.urls = get_urls_from_ids(from_id, to_id, 'disease')
        self.mapping = {}
        super(DiseaseElementaryInfoSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for disease_id, url in self.urls.items():
            self.mapping[url] = disease_id
            yield self.make_requests_from_url(url)

    def parse(self, response):
        symbol = (self.mapping.get(response.url), response.url)
        self.logger.info('Parsing ID.%d 39health Disease Elementary Info From <%s>.' % symbol)

        disease_ele_item = DiseaseElementaryInfoItem()
        try:
            disease_ele_item['d_id'] = symbol[0]
            disease_ele_item['name'] = get_content(response.xpath('//dl[@class="intro"]/dt/text()').extract())
            try:
                relative_drug_path = response.xpath('//div[@class="drug"]/ul/li')
                has_drug = get_content(relative_drug_path[0].xpath('i/text()').extract())
                if self.d_map.has_key(has_drug):
                    drug_list = relative_drug_path[0].xpath('a')
                    dn = []
                    for d in drug_list:
                        dl = get_content(d.xpath('@title').extract())
                        if dl:
                            dn.append(dl)
                    disease_ele_item[self.d_map[has_drug]] = ' '.join(dn)
            except:
                pass

            ele = response.xpath('//div[@class="info"]/ul/li')
            for li in ele:
                attr = get_content(li.xpath('i/text()').extract())
                if self.d_map.has_key(attr):
                    if self.type_map[attr]:
                        label_list = li.xpath('a')
                        ll = []
                        for l in label_list:
                            if l.xpath('@title'):
                                lc = get_content(l.xpath('@title').extract())
                            else:
                                lc = get_content(l.xpath('text()').extract())
                            if lc:
                                ll.append(lc)
                        disease_ele_item[self.d_map[attr]] = ' '.join(ll)
                    else:
                        disease_ele_item[self.d_map[attr]] = get_content(li.xpath('text()').extract())

            return disease_ele_item
        except:
            return None
