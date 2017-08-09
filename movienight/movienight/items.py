# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovienightItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        #Theater Details
    title = scrapy.Field()
    productionid = scrapy.Field()
    rating = scrapy.Field()
    duration = scrapy.Field()
    screenformat = scrapy.Field()
    showtimes = scrapy.Field()
    theater = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    #Movie Details
    director = scrapy.Field()
    producer = scrapy.Field()
    writer = scrapy.Field()
    releasedate = scrapy.Field()
    runtime = scrapy.Field()
    synopsis = scrapy.Field()
    cast = scrapy.Field()
    pass
