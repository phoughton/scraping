import scrapy
import os
import urllib.parse

out_file="results1.json"
if os.path.exists(out_file):
    os.remove(out_file)


class MedicalSpider(scrapy.Spider):
    name = 'medspider'
    start_urls = ["https://www.medicines.org.uk/emc/browse-companies"]

    def parse(self, response):
        # for company_name in response.css('a.key'):

        for alphabet_item in response.css("ul.browse>li>a"):
            yield response.follow(alphabet_item, self.parse)

        for href in response.css("a.key ::attr(href)"):
            yield response.follow(href, self.parse_company_details)
            
    
    def parse_company_details(self, response):
        raw_contact = ' '.join(response.css('div.gfdCompanyDetailsCol ::text').getall())
        yield {
            'companyName': response.css('h1 ::text').get(), 'companyContactDetails': " ".join(raw_contact.split()),
            "image_urls": [urllib.parse.urljoin(response.url,response.css('img.img-responsive::attr(src)').get() )]
        }
        

