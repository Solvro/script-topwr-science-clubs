from dataclasses import fields
from enum import Enum

import scrapy
from itemloaders.processors import MapCompose

from ..items import SciClubItemLoader, SciClubItem, extract_href


class OrgType(Enum):
    SCI_CLUB = "kola-naukowe"
    CULTURAL_AGENCY = "agendy-kultury"
    MEDIA = "media-studenckie"
    ORGANIZATION = "organizacje-studenckie"


class StudentDeptSpider(scrapy.Spider):
    name = "sci_clubs"
    allowed_domains = ["dzialstudencki.pwr.edu.pl"]
    _ROOT = "https://dzialstudencki.pwr.edu.pl/organizacje-studenckie/wykaz-uczelnianych-organizacji-studenckich/"
    SCI_CLUB_SECTION_XPATH = "//div[@class='accordion text-content' and count(*)=2 and button[@class='accordion-title'] and div[@class='accordion-text']]"

    def start_requests(self):
        yield scrapy.Request(self._ROOT + "kola-naukowe")
        # yield scrapy.Request(self._ROOT + "agendy-kultury",
        #                      lambda x: self.parse_detailed_page(x, OrgType.CULTURAL_AGENCY))
        # yield scrapy.Request(self._ROOT + "media-studenckie", lambda x: self.parse_detailed_page(x, OrgType.MEDIA))
        # yield scrapy.Request(self._ROOT + "organizacje-studenckie",
        #                      lambda x: self.parse_detailed_page(x, OrgType.ORGANIZATION))

    def parse(self, response):
        departments = response.xpath("//ul[@class='row columns clearfix no-bullets']/li/div/a")
        for dept in departments:
            name = dept.xpath(".//span[@class='text']/text()").get()
            link = dept.xpath(".//@href").get()
            yield response.follow(link, self.parse_detailed_page,
                                  cb_kwargs={"org_type": OrgType.SCI_CLUB, "department_name": name})

    def parse_detailed_page(self, response, org_type: OrgType, department_name: str = None):
        for sciClub in response.xpath(self.SCI_CLUB_SECTION_XPATH):
            loader = SciClubItemLoader(item=SciClubItem(), selector=sciClub)
            loader.add_xpath('title', ".//button/text()")
            loader.add_xpath('description', ".//div/p[1]//text()")
            loader.add_xpath('description', ".//div/p[2]//text()")

            loader.add_xpath('email', ".//div/p/span/text()",
                             re='Adres e-mail:(.*)')  # pure text (always the case I guess)

            loader.add_xpath('facebook', ".//div/p/span[contains(., 'Facebook:')]",
                             MapCompose(extract_href))  # must be a link

            loader.add_xpath('linkedin', ".//div/p/span[contains(., 'LinkedIn:')]",
                             MapCompose(extract_href))  # must be a link

            loader.add_xpath('website', ".//div/p/span[contains(., 'Strona internetowa:')]",
                             MapCompose(extract_href))  # must be a link
            loader.add_xpath('website', ".//div/p/span//text()", re='Strona internetowa:(.*)')  # pure text

            loader.add_xpath('logotype', ".//div/p/span/img/@src")
            loader.add_xpath('logotype', ".//div/p/img/@src")
            loader.add_value('org_type', org_type.value)
            loader.add_value('department_name', department_name)
            yield loader.load_item()
