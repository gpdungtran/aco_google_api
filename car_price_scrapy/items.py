# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re 
from itemloaders.processors import TakeFirst, MapCompose

"""
ty => trieu "1.73 ty" => 
if "tỷ" in value:
    ty = 1
else:
    ty = 0
1.73
    



1730
"""

#remove the currency
def remove_currency_sign(value):
   
    # python replace method to replace currency with a blank and convert to integer number
    if "tỷ" in value:
        ty = 1
    else:
        ty = 0
    value = value.replace(",",".")    
    re_value = float(re.sub(r'[^0-9(.)]','',str(value)))
    if ty == 1:
        re_value = re_value*1000
    return re_value

class CarPriceScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    
    car_url = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    version = scrapy.Field(output_processor=TakeFirst())
    price_original = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_after = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_1 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_2 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    price_3 = scrapy.Field(input_processor=MapCompose(remove_currency_sign),output_processor=TakeFirst())
    
    
