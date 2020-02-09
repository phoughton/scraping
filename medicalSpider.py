import scrapy
import os

out_file="output1.json"
if os.path.exists(out_file):
    os.remove(out_file)


class MedicalSpider(scrapy.Spider):
    name = 'medspider'
    start_urls = ["https://www.medicines.org.uk/emc/browse-companies"]

    def parse(self, response):
        # for company_name in response.css('a.key'):

        for alphabet_item in response.css("ul.browse>li>a"):
            yield response.follow(alphabet_item, self.parse)

            # company_page = response.css("a.key::attr(href)").get()
        #for company in response.css("a.key"):
         #   yield {'companyName': company.css("a.key ::text").get(), 'companyURL': company.css("a.key ::attr(href)").get()}
        
        for href in response.css("a.key ::attr(href)"):
            yield response.follow(href, self.parse_company_details)
            
    
    def parse_company_details(self, response):
        raw_contact = ' '.join(response.css('div.gfdCompanyDetailsCol ::text').getall())
        yield {'companyName': response.css('h1 ::text').get(), 'companyContactDetails': " ".join(raw_contact.split())}

                
        #yield {'companyName': response.css("a.key:last-child() ::text").get(), 'companyURL': response.css("a.key:last-child() ::attr(href)").get()}

            # if company_page is not None:
            #     company_page = response.urljoin(company_page)
            #     yield scrapy.Request(company_page, callback=self.parse)
            
            #     yield response.follow(company_page, self.parse)
            #     yield {'companyName': response.css('h1 ::text').get()}
