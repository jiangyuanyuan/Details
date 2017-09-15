# -*- coding: utf-8 -*-
import scrapy
from newdongguan.items import NewdongguanItem


class DongdongSpider(scrapy.Spider):
    name = 'xixi'

    allowed_domains = ['kj.cjcp.com.cn']

    url = 'http://kj.cjcp.com.cn/ssq/index.php?topage='
    # http: // kj.cjcp.com.cn / ssq / 2017105.html
    contentUrl = "http://kj.cjcp.com.cn/ssq"
    offset = 1
    start_urls = [url + "1"]


    def parse(self, response):
        # 每一页里的所有帖子的链接集合
        # links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        links = response.xpath('//table[@class="qgkj_table"]//a/@href').extract()
        # 迭代取出集合里的链接
        for link in links:
            if link != '':
                # 提取列表里每个帖子的链接，发送请求放到请求队列里,并调用self.parse_item来处理
                # ../../xinwen/caizhongxinwen-ssq/500159.shtml
                # ./ 2017107.html
                link = link[1:len(link)]
                print link
                yield scrapy.Request("http://kj.cjcp.com.cn/ssq"+link, callback = self.parse_item)

        # 页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 73:
            self.offset += 1
            # 发送请求放到请求队列里，调用self.parse处理response
            # http: // www.zhcw.com / xinwen / caizhongxinwen / index_6.shtml
            yield scrapy.Request(self.url + "index_"+str(self.offset)+".shtml", callback = self.parse)

    # 处理每个帖子的response内容
    def parse_item(self, response):
        item = NewdongguanItem()
        # 标题
        # item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        # try:
        item['title'] = response.xpath('//div[@class="jr_kj"]/h1/text()').extract()[0]
        # 编号
        item['qihao'] = response.xpath('//table[@class="qgkj_table"]//tr[1]/td[2]/text()').extract()[0]
        kaijianhao = response.xpath('//table[@class="qgkj_table"]//tr[1]/td[4]/text()').extract()[0]
        item['kaijianhao'] = str(kaijianhao).replace(" ","").replace("/r/n","")
        item['jiezhiduijianshijian'] = response.xpath('//table[@class="qgkj_table"]//tr[2]/td[2]/text()').extract()[0]
        chuqiushunxu = response.xpath('//table[@class="qgkj_table"]//tr[2]/td[4]/text()').extract()[0]
        item['chuqiushunxu'] = str(chuqiushunxu).replace(" ","")
        item['benqixiaoliang'] = response.xpath('//table[@class="qgkj_table"]//tr[3]/td[2]/text()').extract()[0]
        item['jianchiguncun'] = response.xpath('//table[@class="qgkj_table"]//tr[3]/td[4]/text()').extract()[0]

        item['yidengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[7]/td[2]/text()').extract()[0]
        yidengjianjianjin= response.xpath('//table[@class="qgkj_table"]//tr[7]/td[3]/text()').extract()[0]
        item['yidengjianjianjin'] =str(yidengjianjianjin).replace(" ","").replace("/r/n","")

        # item['erdengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[8]/td[2]/text()').extract()[0]
        item['erdengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[8]/td[@class="qihao t_center"]/span/text()').extract()[0]
        # item['erdengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[8]/td[3]/text()').extract()[0]
        item['erdengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[8]/td[3]/text()').extract()[0]

        # item['sandengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[9]/td[2]/text()').extract()[0]
        item['sandengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[9]/td[@colspan="2"]/span/text()').extract()[0]

        # item['sandengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[9]/td[3]/text()').extract()[0]

        # item['sidengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[10]/td[2]/text()').extract()[0]

        # item['sidengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[10]/td[3]/text()').extract()[0]

        # item['wudengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[11]/td[2]/text()').extract()[0]
        # item['wudengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[11]/td[3]/text()').extract()[0]

        # item['liudengjianzhushu'] = response.xpath('//table[@class="qgkj_table"]//tr[12]/td[2]/text()').extract()[0]
        # item['liudengjianjianjin'] = response.xpath('//table[@class="qgkj_table"]//tr[12]/td[3]/text()').extract()[0]

        # except Exception, e:
        #     print "failue"
        # # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        # contents = response.xpath('//div[@id = "news_main"]//div[@class = "news_content"]//p/text()').extract()
        # content =""
        # for cont in contents:
        #     content = content+cont
        # item['content']= content
        #
        # item['url'] = response.url

        # 交给管道
        yield item

