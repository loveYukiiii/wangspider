import scrapy
from mukespider.items import MukespiderItem


#
# class MySpider(scrapy.Spider):
#     # 用于区别Spider
#     name = "MySpider"
#     # 允许访问的域
#     allowed_domains = ["immoc.com"]
#     # 爬取的地址
#     start_urls = ["https://www.imooc.com/course/list?c=java"]
#
#     # 爬取方法
#     def parse(self, response):
#         item=MukespiderItem()
#         for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
#             item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
#             # 获取div中的课程标题
#             item['title'] = box.xpath('.//h3/text()').extract()
#             # 获取div中的标题图片地址
#             item['image'] = box.xpath('.//@src').extract()
#             # 获取div中的学生人数
#             item['num'] = box.xpath('.//span/text()').extract()
#             # 获取div中的课程简介
#             item['introduction'] = box.xpath('.//p/text()').extract()
#             yield item



class MySpider(scrapy.Spider):
    # 用于区别Spider
    name = "MySpider"
    # 允许访问的域
    # allowed_domains = ["immoc.com"]
    # 爬取的地址
    start_urls = ["https://fitness.pclady.com.cn/"]

    # 爬取方法
    def parse(self, response):
        item=MukespiderItem()
        for box in response.xpath('//div[@class="artCon"]/ul[@class="clearfix"]/li'):
            # 图片跳转链接
            item['url'] = box.xpath('./i[@class="iPic"]//@href').extract()
            # 图片地址
            item['title'] = box.xpath('./i[@class="iPic"]//@src').extract()
            # 获取div中的标题
            item['image'] = box.xpath('./i[@class="iTxt"]/span[@class="sTit"]/em[@class="eTit"]//text()').extract()
            # 获取div中的学生人数
            item['num'] = box.xpath('./i[@class="iTxt"]/span[@class="sDes"]/text()').extract()
            # 获取div中的课程简介
            item['introduction'] = box.xpath('./i[@class="iTxt"]/span[@class="sDes"]//@href').extract()
            yield item

            next_page_url =  response.xpath(
                '//div[@class="artCon"]/div[@class="artPages"]/div[@class="pclady_page"]/a[@class="next"]//@href').extract()[0]
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))