# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewdongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 编号
    qihao = scrapy.Field()
    # 内容
    kaijianhao = scrapy.Field()
    # 链接
    jiezhiduijianshijian = scrapy.Field()
    # 出球顺序
    chuqiushunxu = scrapy.Field()
    # 本期销量
    benqixiaoliang = scrapy.Field()
    jianchiguncun = scrapy.Field()
    # 一等奖
    yidengjianzhushu = scrapy.Field()
    yidengjianjianjin = scrapy.Field()
    # 二等奖
    erdengjianzhushu = scrapy.Field()
    erdengjianjianjin = scrapy.Field()
    # 三等
    sandengjianzhushu = scrapy.Field()
    sandengjianjianjin = scrapy.Field()
    # 四等奖
    # 四等奖
    sidengjianzhushu = scrapy.Field()
    sidengjianjianjin = scrapy.Field()

    wudengjianzhushu = scrapy.Field()
    wudengjianjianjin = scrapy.Field()

    liudengjianzhushu = scrapy.Field()
    liudengjianjianjin = scrapy.Field()
