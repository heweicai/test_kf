# _*_ coding: utf-8 _*_
import scrapy
from govinfos.items import GovinfosItem


class GovInfos(scrapy.Spider):

    # 启动爬虫的名称
    name = 'govinfo'
    # 爬虫的范围
    allowed_domains=['xzqh.mca.gov.cn']

    # 爬虫的第一个url
    # start_urls = ['http://xzqh.mca.gov.cn/fuzzySearch']

    # 这里是用post请求数据的
    def start_requests(self):
        url = 'http://xzqh.mca.gov.cn/fuzzySearch'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {"fs" : "%"},
            callback = self.parse
        )

    # 爬取结果分析
    def parse(self, response):
        print('%'*30)

        # print(response.body)
        node_list = response.xpath("//*[@class='info_table']/tr")
        for node in node_list:

            # 根据jiansuo_table 进行判断是否包含，若不包含，则为城市的第一个名称
            # 第一个城市的第一个名称
            td1 = node.xpath("./td[@class='name_left']/a/text()").extract()

            shen_address = node.xpath("./td/table[@class='jiansuo_table']/tr[@class='name_left']/td/a[@class='sheng_td']/text()").extract()
            shi_address = node.xpath("./td/table[@class='jiansuo_table']/tr[@class='name_left']/td/a[@class='shi_td']/text()").extract()
            qu_address = node.xpath("./td/table[@class='jiansuo_table']/tr[@class='name_left']/td[3]/a/text()").extract()
            print('%' * 30)
            print(td1)
            print(shen_address)
            print(shi_address)
            print(qu_address)

            # 驻地
            zhudi_address =node.xpath("./td[@class='name_left']/text()").extract()
            print(zhudi_address)
            # renkou
            person = node.xpath("./td[3]/text()").extract()
            print(person)
            #面积
            area = node.xpath("./td[4]/text()").extract()
            print(area)
            # 行政区划
            xingzhen = node.xpath("./td[5]/text()").extract()
            print(xingzhen)
            # 区号
            quhao = node.xpath("./td[6]/text()").extract()
            print(quhao)
            # 邮编
            # print(node)
            youbian = node.xpath("./td[7]/text()").extract()
            print(youbian)