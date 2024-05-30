import scrapy
from itemloaders.processors import MapCompose

from models.org_type import OrgType
from models.scraped_item import SciClubItem, SciClubItemLoader

from ..extract_href import extract_href


class SciClubsSpider(scrapy.Spider):
    name = "sci_clubs"
    allowed_domains = ["dzialstudencki.pwr.edu.pl"]
    _SCI_CLUB_SECTION_XPATH = (
        "//div[@class='accordion text-content' and count(*)=2 and button"
        "[@class='accordion-title'] and div[@class='accordion-text']]"
    )
    _ROOT = "https://dzialstudencki.pwr.edu.pl/organizacje-studenckie/wykaz-uczelnianych-organizacji-studenckich/"

    def _get_detail_request(self, org_type: OrgType):
        return scrapy.Request(
            self._ROOT + org_type.value[0],
            self.parse_detail_page,
            cb_kwargs={"org_type": org_type},
        )

    def start_requests(self):
        yield scrapy.Request(self._ROOT + OrgType.SCI_CLUB.value[0])
        yield self._get_detail_request(OrgType.CULTURAL_AGENCY)
        yield self._get_detail_request(OrgType.MEDIA)
        yield self._get_detail_request(OrgType.ORGANIZATION)

    def parse(self, response, **kwargs):
        departments = response.xpath(
            "//ul[@class='row columns clearfix no-bullets']/li/div/a"
        )
        for dept in departments:
            name = dept.xpath(".//span[@class='text']/text()").get()
            link = dept.xpath(".//@href").get()
            yield response.follow(
                link,
                self.parse_detail_page,
                cb_kwargs={
                    "org_type": OrgType.SCI_CLUB,
                    "department_name": name,
                },
            )

    @staticmethod
    def add_social_link(loader, field, keyword, text):
        loader.add_xpath(
            field,
            f".//div/p/span[contains(., '{text}:')]",
            MapCompose(lambda x: extract_href(x, keyword)),
        )  # must be a link
        loader.add_xpath(field, ".//div/p/span//text()", re=f"{text}:(.*)")  # pure text
        loader.add_value(
            field, extract_href(loader.selector.get(), keyword)
        )  # any link with keyword

    @staticmethod
    def add_webpage(loader, field, text):
        loader.add_xpath(
            field,
            f".//div/p/span[contains(., '{text}:')]",
            MapCompose(lambda x: extract_href(x, "")),
        )  # must be a link
        loader.add_xpath(field, ".//div/p/span//text()", re=f"{text}:(.*)")  # pure text

    def parse_detail_page(
        self, response, org_type: OrgType, department_name: str = None
    ):
        for sciClub in response.xpath(self._SCI_CLUB_SECTION_XPATH):
            loader = SciClubItemLoader(item=SciClubItem(), selector=sciClub)
            loader.add_xpath("name", ".//button/text()")

            loader.add_xpath("description", ".//div/p[1]//text()")
            loader.add_xpath("description", ".//div/p[2]//text()")

            loader.add_xpath(
                "email", ".//div/p/span/text()", re="Adres e-mail:(.*)"
            )  # pure text (always the case I guess)

            self.add_social_link(loader, "facebook", "facebook", "Facebook")
            self.add_social_link(loader, "linkedin", "linkedin", "LinkedIn")
            self.add_social_link(loader, "instagram", "instagram", "Instagram")
            self.add_social_link(loader, "tiktok", "tiktok", "Tik-Tok")
            self.add_webpage(loader, "website", "Strona internetowa")
            self.add_webpage(loader, "website", "Strona")
            self.add_webpage(loader, "website", "Strona .*?")

            loader.add_xpath("logo", ".//div/p/span/img/@src")
            loader.add_xpath("logo", ".//div/p/img/@src")

            loader.add_value("type", org_type.value[0])
            loader.add_value("department_name", department_name)

            yield loader.load_item()
