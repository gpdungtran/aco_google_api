# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re 
from itemloaders.processors import TakeFirst, MapCompose

def remove_currency_sign(value):
   
    # python replace method to replace currency with a blank
    return re.sub(r'[^0-0.]','',str(value))
    #return value


class CarPriceScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_url = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    price_1 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_2 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_3 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
