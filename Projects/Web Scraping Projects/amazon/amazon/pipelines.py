# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonPipeline:
    def process_item(self, item, spider):
        rating_text = item['rating']
        rating_number = rating_text[0:3]
        item['rating'] = rating_number
        return item
