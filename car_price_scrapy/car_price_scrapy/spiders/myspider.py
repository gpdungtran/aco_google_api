import scrapy
from car_price_scrapy.items import CarPriceScrapyItem

class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["clever-lichterman-044f16.netlify.app"]
    start_urls = ["https://clever-lichterman-044f16.netlify.app/products/taba-cream.1/"]

    def parse(self, response):
       pass 
