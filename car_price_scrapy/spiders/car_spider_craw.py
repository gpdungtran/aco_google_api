from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Import the Item Loader library
from scrapy.loader import ItemLoader

from ..items import CarPriceScrapyItem


class CarSpiderCrawSpider(CrawlSpider):
    name = "car_spider_craw"
    allowed_domains = ["danchoioto.vn"]
    start_urls = ["https://danchoioto.vn/gia-xe-honda-crv/"]
    rules = (
        Rule(
            LinkExtractor(
                allow='gia-xe',
            ),
            callback='parse',
            follow=True
        ),
    )
    #rules = (Rule(LinkExtractor()),)

    def parse(self, response):
        # Define your XPath or CSS selector to locate the table

        table_rows = response.xpath('//table[1]/tbody/tr')

        # Define the Itemloader
        #loader = ItemLoader(item=CarPriceScrapyItem(), selector=table_rows)        
        
        # Initialize an empty dictionary to store the data
        #data_dict = {}
        #data_dict['url'] = response.url
        #loader.add_value('car_url',response.url) 
        for row in table_rows[1:]:  # Skip the header row
            # Extract data from each column of the row
            columns = row.xpath('.//td')
            row_data = [column.xpath('normalize-space(.)').get() for column in columns]

            # Assuming the first column is the key and the second column is the value
            #key = row_data[0]
            #value = row_data[1:4]
            loader = ItemLoader(item=CarPriceScrapyItem(), selector=table_rows)
            loader.add_value('car_url',response.url)
            # Add the key-value pair to the dictionary
            #data_dict[key] = value
            print(row_data)
            loader.add_value('name',str(row_data[0]))
            loader.add_value('price_1',str(row_data[1]))
            loader.add_value('price_2',str(row_data[2]))
            loader.add_value('price_3',str(row_data[3]))

        # Yield or return the dictionary
        # print(data_dict)
            yield loader.load_item()
    #print(data_dict)
