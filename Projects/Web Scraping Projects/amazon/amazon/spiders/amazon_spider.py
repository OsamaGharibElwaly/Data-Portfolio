import scrapy
import logging
from ..items import AmazonItem

# Set log level for asyncio module to WARNING
logging.getLogger('asyncio').setLevel(logging.WARNING)


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.eg']
    page_number = 2
    start_urls = [
        'https://www.amazon.eg/-/en/s?i=electronics&rh=n%3A18018102031&fs=true&page=5&qid=1712587966&ref=sr_pg_5'
        
    ]



    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-text-normal::text').extract()
        price = response.css('.a-price-whole::text').extract()
        rating = response.css('span.a-icon-alt::text').extract()
        product_image = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['price'] = price
        items['rating'] = [r[:3] for r in rating]
        items['product_image'] = product_image

        yield items
