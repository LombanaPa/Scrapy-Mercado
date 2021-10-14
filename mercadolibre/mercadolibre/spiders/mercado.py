import scrapy


class MercadoSpider(scrapy.Spider):
    name = 'mercado'
    allowed_domains = ['www.mercadolibre.com.co']
    start_urls = ['https://listado.mercadolibre.com.co/impresoras#D[A:impresoras]']

    def parse(self, response):
        impresora = response.xpath("//h2[@class='ui-search-item__title']/text()").extract()
        precio = response.xpath("//span[@class='price-tag-fraction']/text()").extract()

        for item in zip(impresora,precio):
            scraped_info = {
                'Impresora': item[0],
                'Precio': item[1]
            }
            yield scraped_info

from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter

class MyProjectCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = get_project_settings.get('CSV_DELIMITER', '|')
        kwargs['delimiter'] = delimiter

        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
        	kwargs['fields_to_export'] = fields_to_export

        super(MyProjectCsvItemExporter, self).__init__(*args, **kwargs)
