__author__ = 'linweihua'

import scrapy
from utils.webpage import get_content

class CFDAHelperSpider(scrapy.Spider):
    name = 'cfda'
    allowed_domains = ['http://app1.sfda.gov.cn/']
    post_url = 'http://app1.sfda.gov.cn/datasearch/face3/search.jsp'
    pipeline = ['UniqueItemPersistencePipeline']

    def __init__(self, from_id=1, to_id=1, *args, **kwargs):
        to_id = max(int(from_id), int(to_id))
        self.shortlist = xrange(int(from_id), int(to_id)+1)
        super(CFDAHelperSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        header = {
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=C1D7E1F63DD146308CDB66FCD0A81165.7; _gscu_1586185021=664790034cqbpt82; _gscs_1586185021=66479003lcl77s82 \
|pv:1; _gscbrs_1586185021=1',
            'Referer': 'http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=25&tableName=TABLE25&title=%B9%FA%B2%FA%D2%A9%C6%B7&bcId=124356560303886909015737447882',
            'Content-Type': 'application/x-www-form-urlencoded',
            #'Content-Length': 273,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',
            'Host': 'app1.sfda.gov.cn',
            'Cache-Control': 'no-cache',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
        }
        cookie = {
            'JSESSIONID': 'C1D7E1F63DD146308CDB66FCD0A81165.7',
            '_gscu_1586185021': '664790034cqbpt82',
            '_gscs_1586185021': '66479003lcl77s82|pv:1',
            '_gscbrs_1586185021': 1,
        }

        for i in self.shortlist:
            yield scrapy.http.Request(
                self.post_url,
                method='POST',
                headers=header,
                cookies=cookie,
                meta= {
                    "tableId": '25',
                    "State": '1',
                    "bcId": "124356560303886909015737447882",
                    "tableName": "TABLE25",
                    "viewtitleName": "COLUMN167",
                    "viewsubTitleName": "COLUMN166,COLUMN170,COLUMN821",
                    "curstart": str(i),
                    "tableView": "%E5%9B%BD%E4%BA%A7%E8%8D%AF%E5%93%81",
                }
            )

    def parse(self, response):
        print response.status, response.body