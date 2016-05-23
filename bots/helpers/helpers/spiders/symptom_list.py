__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content
from helpers.items import SymptomItem

class SymptomListSpider(scrapy.Spider):
    name = 'symptom'
    allowed_domains = ['http://jbk.39.net']
    first_url = 'http://jbk.39.net/bw_t2'
    start_formated_url = 'http://jbk.39.net/bw_t2_p{page_id}#ps'

    def __init__(self, from_id=1, to_id=1, *args, **kwargs):
        to_id = max(int(from_id), int(to_id))
        self.shortlist = xrange(int(from_id), int(to_id)+1)
        super(SymptomListSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        yield self.make_requests_from_url(self.first_url)
        for i in self.shortlist:
            url = self.start_formated_url.format(page_id=i)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Parsing 39 Symptom URLs From <%s>.' % response.url)

        item_list = []
        elements = response.xpath('//div[@class="res_list"]')
        for ele in elements:
            item = SymptomItem()
            item['name'] = get_content(ele.xpath('dl/dt/h3/a/text()').extract())
            item['link'] = get_content(ele.xpath('dl/dt/h3/a/@href').extract())
            try:
                item['alias'] = get_content(ele.xpath('dl/dt/cite/text()').extract())
                disease_list = ele.xpath('div/p/a')
                relevant_diseases = []
                for d in disease_list:
                    rd = get_content(d.xpath('text()').extract())
                    if rd: relevant_diseases.append(rd)
                item['relevant_diseases'] = ' '.join(relevant_diseases)
            except:
                pass
            item_list.append(item)

        return item_list


