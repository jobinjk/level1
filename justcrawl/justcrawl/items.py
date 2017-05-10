# -*- coding: utf-8 -*-

# Define here the models for your scraped items
import scrapy
from scrapy.item import Item, Field
class Website(Item):
    product_name = Field()
    price = Field()