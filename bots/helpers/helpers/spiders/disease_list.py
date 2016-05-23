__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from helpers.items import DiseaseItem

class DiseaseListSpider(scrapy.Spider):
    name = 'disease'
    allowed_domains = ['http://jbk.39.net']
    first_url = 'http://jbk.39.net/bw_t1'
    start_formated_url = 'http://jbk.39.net/bw_t1_p{page_id}#ps'
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id=1, to_id=1, *args, **kwargs):
        to_id = max(int(from_id), int(to_id))
        self.shortlist = xrange(int(from_id), int(to_id)+1)
        super(DiseaseListSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        yield self.make_requests_from_url(self.first_url)
        for i in self.shortlist:
            url = self.start_formated_url.format(page_id=i)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Parsing 39 Disease URLs From <%s>.' % response.url)

        item_list = []
        elements = response.xpath('//div[@class="res_list"]')
        for ele in elements:
            item = DiseaseItem()
            item['name'] = get_content(ele.xpath('dl/dt/h3/a/text()').extract())
            item['link'] = get_content(ele.xpath('dl/dt/h3/a/@href').extract())
            try:
                item['alias'] = get_content(ele.xpath('dl/dt/cite/text()').extract())
                symptoms_list = ele.xpath('div/p/a')
                relevant_symptoms = []
                for s in symptoms_list:
                    rs = get_content(s.xpath('text()').extract())
                    if rs:
                        relevant_symptoms.append(rs)
                item['relevant_symptoms'] = ' '.join(relevant_symptoms)
            except:
                pass
            item_list.append(item)

        return item_list


