# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from tinydeal.items import TinydealItem


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    url = 'https://www.tinydeal.com/specials.html'
    min_price = 0
    max_price = 0

    def start_requests(self):
        yield scrapy.Request(
            url=self.url + '?disp_order=15&is_input=1&pfrom={0}&pto={1}'.format(self.min_price, self.max_price),
            callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/76.0.3809.100 Safari/537.36'
            })

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            loader = ItemLoader(item=TinydealItem(), selector=product)
            loader.add_xpath('TITLE_GOODS', ".//a[@class='p_box_title']/text()")
            loader.add_xpath('image_urls', ".//a[@class='p_box_img']/img/@data-original")
            loader.add_xpath('URL_PRODUCT', ".//a[@class='p_box_title']/@href")
            loader.add_xpath('START_PRICE', ".//div[@class='p_box_price']/span[2]/text()")
            loader.add_xpath('DISCO_PRICE', ".//div[@class='p_box_price']/span[1]/text()")
            loader.add_xpath('STARS_RATED', ".//div[@class='p_box_star']/span/@class")
            yield loader.load_item()

        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/76.0.3809.100 Safari/537.36'
            })
