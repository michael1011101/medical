# -*- coding: utf-8 -*-
__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from bots.cfda.cfda.items import CFDADrug

class CFDASpider(scrapy.Spider):
    name = 'cfda'
    allowed_domains = ['http://app1.sfda.gov.cn/']
    start_formated_url = 'http://app1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=25&tableName=TABLE25&tableView=%E5%9B%BD%E4%BA%A7%E8%8D%AF%E5%93%81&Id={page_id}'
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id=1, to_id=1, *args, **kwargs):
        to_id = max(int(from_id), int(to_id))
        self.shortlist = xrange(int(from_id), int(to_id)+1)
        super(CFDASpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for i in self.shortlist:
            url = self.start_formated_url.format(page_id=i)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Parsing cfda drug info From <%s>.' % response.url)
        item = CFDADrug()

        elements = response.xpath('//div[@class="listmain"]/div/table[1]/tr')

        if len(elements) > 13:
            item['url_id'] = int(response.url.split('=')[-1])
            item['approval_num'] = get_content(elements[1].xpath('td[2]/text()').extract())
            item['name'] = get_content(elements[2].xpath('td[2]/text()').extract())
            item['en_name'] = get_content(elements[3].xpath('td[2]/text()').extract())
            item['trade_name'] = get_content(elements[4].xpath('td[2]/text()').extract())
            item['dosage_forms'] = get_content(elements[5].xpath('td[2]/text()').extract())
            item['norm'] = get_content(elements[6].xpath('td[2]/text()').extract())
            item['producer'] = get_content(elements[7].xpath('td[2]/a/text()').extract())
            item['product_address'] = get_content(elements[8].xpath('td[2]/text()').extract())
            item['type'] = get_content(elements[9].xpath('td[2]/text()').extract())
            item['origin_approval_num'] = get_content(elements[10].xpath('td[2]/text()').extract())
            item['approval_date'] = get_content(elements[11].xpath('td[2]/text()').extract())
            item['drug_based_code'] = get_content(elements[12].xpath('td[2]/text()').extract())
            item['remark'] = get_content(elements[13].xpath('td[2]/text()').extract())
            return item
        else:
            return None