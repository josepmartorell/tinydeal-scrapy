# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class TinydealItem(scrapy.Item):
    TITLE_GOODS = scrapy.Field(
        output_processor=TakeFirst()
    )
    IMAGE_GOODS = scrapy.Field()
    URL_PRODUCT = scrapy.Field()
    START_PRICE = scrapy.Field()
    DISCO_PRICE = scrapy.Field()
    STARS_RATED = scrapy.Field()
    pass
