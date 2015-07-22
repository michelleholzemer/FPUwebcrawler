from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class firstSpider(BaseSpider):
    name = "fpu"
    allowed_domains = ["floridapolytechnic.org"]
    start_urls = ["https://www.floridapolytechnic.org/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//div")

        for titles in titles:
            title = titles.select("a/@href").extract
            print link
