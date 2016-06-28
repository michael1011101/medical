# -*- coding: utf-8 -*-
__author__ = 'wangchaohui'

import scrapy
from utils.webpage import get_content
from _39.items import XinwenItem
from bots.helpers.helpers.items import NewsListItem

#############################################################################################
#                                                                                           #
# USAGE: nohup scrapy crawl xinwen -a from_id =1 -a to_id=1 --loglevel=INFO --logfile=log & #
#                                                                                           #
#############################################################################################

class XinwenSpider(scrapy.Spider):
	name = 'xinwen'
	allowed_domains = ['http://news.39.net']
	pipeline = ['RelatedItemPersistencePipeline']

	def __init__(self, from_id=1, to_id=1, *args, **kwargs):
		self.mapping = {}
		self.shortlist = xrange(int(from_id), int(to_id)+1)
		super(XinwenSpider, self).__init__(*args, **kwargs)

	def start_requests(self):
		for i in self.shortlist:
			obj = NewsListItem.get_object_by_pk(i)
			self.mapping[obj.link] = obj.id
			# print self.make_requests_from_url(obj.link)
			# input()
			try:
				yield self.make_requests_from_url(obj.link)
			except Exception, e:
				pass
			

	def parse(self, response):
		symbol = (self.mapping.get(response.url), response.url)
		self.logger.info("Parsing ID.%d 39Health News Disease Ditail From <%s>" % symbol)
		self.object = NewsListItem.get_object_by_pk(symbol[0])

		item = XinwenItem()
		left = response.xpath('//div[@class="art_left"]')
		if left:
			item['title'] = get_content(left.xpath('div/h1/text()').extract())

			info = left.xpath('div/div[@class="art_info"]')
			detail = info.xpath('div[@class="date"]//em')
			item['time'] = get_content(detail[0].xpath('text()').extract())
			
			source = detail[1].xpath('a')
			if source:
				item['source_website_link'] = get_content(source.xpath('@href').extract())
				item['source_website'] = get_content(source.xpath('text()').extract())
			else:
				item['source_website'] = get_content(detail[1].xpath('text()').extract())

			item['source_author'] = get_content(detail[2].xpath('text()').extract(), skipBlank=False);
			
			item['summary'] = get_content(left.xpath('div/p[@class="summary"]/text()').extract())
			item['content'] = get_content(left.xpath('div/div[@class="art_con"]').extract())
		return item