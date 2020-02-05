import scrapy
import os

os.remove("output1.json")


class MedicalSpider(scrapy.Spider):
    name = 'medspider'
    start_urls = ["https://www.medicines.org.uk/emc/browse-companies"]

    def parse(self, response):
        # for company_name in response.css('a.key'):

        for alphabet_item in response.css("ul.browse>li>a"):
            yield response.follow(alphabet_item, self.parse)

            # company_page = response.css("a.key::attr(href)").get()
        for company in response.css("a.key"):
            yield {'companyName': company.css("a.key ::text").get(), 'companyURL': company.css("a.key ::attr(href)").get()}
        #yield {'companyName': response.css("a.key:last-child() ::text").get(), 'companyURL': response.css("a.key:last-child() ::attr(href)").get()}

            # if company_page is not None:
            #     company_page = response.urljoin(company_page)
            #     yield scrapy.Request(company_page, callback=self.parse)
            
            #     yield response.follow(company_page, self.parse)
            #     yield {'companyName': response.css('h1 ::text').get()}
