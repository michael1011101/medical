__author__ = 'wangchaohui'

import scrapy
from utils.webpage import get_content
from helpers.items import NewsListItem

##############################################################################################################
#                                                                                                            #
# USAGE: nohup scrapy crawl news_list -a from_id =1 -a to_id=1 -a category=1 --loglevel=INFO --logfile=log & #
#                                                                                                            #
##############################################################################################################

class NewsListSpider(scrapy.Spider):
    name = 'news_list'
    allowed_domains = ['http://news.39.net']
    first_url = 'http://news.39.net/{category}/index.html'
    start_formated_url = 'http://news.39.net/{category}/index_{page_id}.html'
    tab = ['', 'jbyw', 'yltx', 'medicine', 'kyfx', 'shwx', 'qwfb', 'jjyg', 'mxrd', 'qwqs', 'hygc', \
           'interview', 'ysbj/ys', 'hxw/hyp', 'hxw/hsp', 'hxw/hyaop']
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id=1, to_id=1,  category=1, *args, **kwargs):
        self.shortlist = xrange(int(from_id)-1, int(to_id))
        self.category_id = int(category)
        self.category = self.tab[int(category)]
        super(NewsListSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for i in self.shortlist:
            if i == 0:
                url = self.first_url.format(category=self.category)
            else:
                url = self.start_formated_url.format(category=self.category, page_id=i)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Parsing 39Health News Disease URLs From <%s>.' % response.url)

        item_list = []
        elements = response.xpath('//div[@class="listbox"]//ul')

        for ele in elements:
            detail_list = ele.xpath('li')
            for detail in detail_list:
                item = NewsListItem()
                item['category_id'] = self.category_id
                item['link'] = get_content(detail.xpath('span/a/@href').extract())
                item['title'] = get_content(detail.xpath('span')[0].xpath('a/text()').extract())
                item['time'] = get_content(detail.xpath('span')[1].xpath('text()').extract(), skipBlank=False)
                item_list.append(item)
        return item_list