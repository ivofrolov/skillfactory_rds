from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from carwler.items import CarSpecification
from carwler.item_loaders import AutoruCarSpecLoader


class AutoruCatalogSpider(CrawlSpider):
    """Extracts cars technical parameters."""
    name = 'autoru_catalog'
    allowed_domains = ('auto.ru',)
    start_urls = (
        'https://auto.ru/htmlsitemap/mark_model_tech_1.html',
        'https://auto.ru/htmlsitemap/mark_model_tech_2.html',
        'https://auto.ru/htmlsitemap/mark_model_tech_3.html',
        'https://auto.ru/htmlsitemap/mark_model_tech_4.html',
        'https://auto.ru/htmlsitemap/mark_model_tech_5.html',
        'https://auto.ru/htmlsitemap/mark_model_tech_6.html',
    )
    rules = (
        Rule(LinkExtractor(allow=('catalog/cars/.+',)), callback='parse_item'),
    )

    def parse_item(self, response):
        loader = AutoruCarSpecLoader(item=CarSpecification())

        loader.add_value('title', response.meta.get('link_text'))

        qual_list = response.css('.search-form-v2-mmm__breadcrumbs a::text').getall()
        for index, field in enumerate(('brand', 'model', 'generation', 'body_type')):
            loader.add_value(field, qual_list[index])

        mod = response.css('.catalog-table__row_active a::text').get()
        loader.add_value('modification', mod)
        
        spec_selector = response.css('.catalog__details-group dl')
        spec_list = spec_selector.css('dt::text, dd::text').getall()
        
        spec_fields = set(loader.item.fields) - {'title', 'rating', 'brand', 'model', 'generation', 'body_type'}
        for field in spec_fields:
            loader.add_value(field, spec_list)  # field processor will find proper spec
        
        return loader.load_item()
