# level1
# item.py
# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy
from scrapy.item import Item, Field
class Website(Item):
    company = scrapy.Field()
    date = scrapy.Field()
    
