from scrapy.spider import Spider
from scrapy.selector import Selector
from justcrawl.items import Website


class JustCrawlSpider(Spider):
    name = "productdetails"
    allowed_domains = ["myntra.com"]
    start_urls = [
                   "https://www.myntra.com/men-tshirts?src=tNav"
    ]

    def parse(self, response):
        
        sel = Selector(response)
        sites = sel.xpath(".//*/div[@class='row-base']")
        items = []

        for site in sites:
            item = Website()
            item['product_name'] = site.xpath("ul/li[i]/a/div/h2").extract()
            item['price'] = site.xpath("div[2]/span[1]/text()[2]").extract()
            
            items.append(item)

        return items