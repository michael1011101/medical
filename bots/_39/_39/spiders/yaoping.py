# -*- coding: utf-8 -*-
__author__ = 'wangchaohui'

import scrapy
from utils.webpage import get_content, get_trunk
from _39.items import YaopingItem

#########################################################################################################################
#                                                                                                                       #
# USAGE: nohup scrapy crawl yaoping -a from_id =1 -a to_id=1 -a file_name=manual_id.txt --loglevel=INFO --logfile=log & #
#                                                                                                                       #
#########################################################################################################################

class YaopingSpider(scrapy.Spider):
	name = 'yaoping'
	allowed_domains = ['http://ypk.39.net/']
	start_formated_url = 'http://ypk.39.net/{manual_id}/manual'
	pipeline = ['UniqueItemPersistencePipeline']
	detail_map = {u'【成份】':'drug_components', u'【主要原料】':'drug_components', u'【功能主治】':'major_function', u'【适应症】':'indication', u'【用法用量】':'usages', \
				  u'【不良反应】':'untoward_reaction', u'【禁忌】':'contradication', u'【注意事项】':'info', u'【特殊人群用药】':'special_crowd_medications',               \
				  u'【药理作用】':'properties', u'【保健功能】':'properties', u'【贮藏】':'store', u'【贮藏方法】':'store', u'【保质期】':'validity',                       \
				  u'【有效期】':'validity', u'【批准文号】':'approval_num', u'【说明书修订日期】':'manual_revision_date'}

	def __init__(self, from_id=1, to_id=10, file_name="manual_id.txt", *args, **kwargs):
		self.mapping = {}
		self.shortlist = self.get_manual_id(file_name, int(from_id), int(to_id)+1)
		super(YaopingSpider, self).__init__(*args, **kwargs)

	def get_manual_id(self, file_name, from_id, to_id):
		File = open(file_name, "r");
		manual_id_list = []
		index = 0
		for line in File:
			index += 1
			if from_id<= index < to_id:
				manual_id_list.append(line.strip());
			if index >= to_id:
				break
		return manual_id_list

	def start_requests(self):
		for i in self.shortlist:
			# obj = YaopingHelpItem.get_object_by_pk(i)
			# if obj:
			url = self.start_formated_url.format(manual_id = int(i))
			self.mapping[url] = int(i)
			yield self.make_requests_from_url(url)

	def parse(self, response):
		# self.object = self.mapping.get(response.url)
		# symbol = (self.object.manual_id, response.url)
		# self.logger.info("Parsing ID.%d 39Health Drug Informations From <%s>." % symbol)

		symbol = (self.mapping.get(response.url), response.url)
		self.logger.info("Parsing ID.%d 39Health Drug Informations From <%s>." % symbol)

		item = YaopingItem()
		item['manual_id'] = symbol[0]

		sub = response.xpath('//div[@class="subs"]//a')
		item['category_list'] = '>>'.join([get_trunk(s) for s in sub.xpath('text()').extract()])

		category_list = item['category_list'].split(">>")
		if len(category_list) == 3:
			item['category_first'] = category_list[1]
		elif len(category_list)  == 4:
			item['category_first'] = category_list[1]
			item['category_second'] = category_list[2]

		item['name'] = get_content(response.xpath('//div[@class="t1"]/h1/a/text()').extract())
		cites = response.xpath('//div[@class="t1"]//cite')
		item['cites'] = '&&'.join([get_trunk(cite) for cite in cites.xpath('span/text()').extract()])

		item['english_name'] = get_content(response.xpath('//cite[@class="t2"]/text()').extract(), skipBlank=False)

		item['company'] = get_content(response.xpath('//li[@class="company"]/text()').extract())
		item['address'] = get_content(response.xpath('//li[@class="address"]/text()').extract())
		item['telephone'] = get_content(response.xpath('//li[@class="telephone"]/text()').extract(), skipBlank=False)

		information = response.xpath('//div[@class="tab_box"]//dl')
		for info in information:
			key = get_content(info.xpath('dt/text()').extract())
			if self.detail_map.get(key):
				attr = self.detail_map[key]
				detail = info.xpath('dd')

				#using string(.) to remove html label
				item[attr] = get_content(detail.xpath('string(.)').extract()) 

		return item