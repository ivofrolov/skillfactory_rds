from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from carwler.items import CarSpecification
from carwler.item_loaders import AutoruCarSpecLoader


class AutoruCatalogSpider(CrawlSpider):
    """Extracts cars technical parameters."""
    name = 'autoru_catalog'
    allowed_domains = ('auto.ru',)
    start_urls = (
        'https://auto.ru/htmlsitemap/mark_model_generation_1.html',
        'https://auto.ru/htmlsitemap/mark_model_generation_2.html',
    )
    rules = (
        Rule(LinkExtractor(allow=('/catalog/cars/.+',)), callback='parse_car_gen'),
    )

    def parse_car_gen(self, response):
        loader = AutoruCarSpecLoader(item=CarSpecification(), selector=response)

        name_loader = loader.nested_css('.search-form-v2-mmm__breadcrumbs')
        for index, field in enumerate(('brand', 'model', 'generation', 'body_type'), start=1):
            name_loader.add_xpath(field, f'./a[{index}]/text()')
        
        loader.add_css('rating', '.catalog-generation__rating-circle-number::text')
        loader.add_css('reviews_count', '.reviews-summary__reviews-count::text', re=r'\d+')

        item = loader.load_item()
        
        return response.follow(
            url='specifications/', callback=self.extract_spec_urls, cb_kwargs=dict(item=item))

    def extract_spec_urls(self, response, item):
        for spec_url in response.css('.catalog-table_packages a.catalog-tab-item::attr(href)').getall():
            yield response.follow(url=spec_url, callback=self.parse_spec, cb_kwargs=dict(item=item.deepcopy()))

    def parse_spec(self, response, item):
        loader = AutoruCarSpecLoader(item=item)

        mod = response.css('.catalog-table__row_active a::text').get()
        loader.add_value('modification', mod)
        
        gen_fields = {'rating', 'reviews_count', 'brand', 'model', 'generation', 'body_type', 'modification'}
        spec_fields = set(loader.item.fields) - gen_fields
        spec_list = [el.css('::text').get() for el in response.css('.catalog__details-group dl').css('dt, dd')]
        for field in spec_fields:
            loader.add_value(field, spec_list)  # field processor will find proper spec
        
        return loader.load_item()
