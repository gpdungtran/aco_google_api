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

        # obtain name_car from first row
        columns = table_rows[0].xpath('.//td')
        row_data = [column.xpath('normalize-space(.)').get() for column in columns]
        name_car = row_data[0]
         
        for row in table_rows[1:]:  # Skip the header row
            # Extract data from each column of the row
            columns = row.xpath('.//td')
            row_data = [column.xpath('normalize-space(.)').get() for column in columns]

            
            # Define the Itemloader
            loader = ItemLoader(item=CarPriceScrapyItem(), selector=table_rows)
            
            # Add the key-value pair to the dictionary
            #data_dict[key] = value
            
            loader.add_value('name',str(name_car))
            loader.add_value('version',str(row_data[0]))
            if (len(row_data)==5):
                loader.add_value('price_original',str(row_data[1]))
                loader.add_value('price_1',str(row_data[2]))
                loader.add_value('price_2',str(row_data[3]))
                loader.add_value('price_3',str(row_data[4]))
            elif len(row_data)==4:
                loader.add_value('price_original',str(row_data[0]))
                loader.add_value('price_1',str(row_data[1]))
                loader.add_value('price_2',str(row_data[2]))
                loader.add_value('price_3',str(row_data[3]))
            elif len(row_data)==3:
                loader.add_value('price_original',str(row_data[1]))
                loader.add_value('price_after',str(row_data[2]))
            elif len(row_data)==2:
                loader.add_value('price_original',str(row_data[1]))
            else:
                pass
            
            loader.add_value('car_url',str(response.url))
        # Yield or return the dictionary
        # print(data_dict)
            yield loader.load_item()
    #print(data_dict)
