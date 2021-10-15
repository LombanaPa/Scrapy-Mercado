import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter
from scrapy import Request

class MercadoSpider(scrapy.Spider):
    name = 'mercado'
    allowed_domains = ['www.mercadolibre.com.co']
    st_url=['https://listado.mercadolibre.com.co/impresoras_NoIndex_True']
    next=["https://listado.mercadolibre.com.co/impresoras_Desde_{0}_NoIndex_True"\
        .format(x) for x in range(51,201,50)]
    
    for i in next:
        st_url.append(i)

    start_urls = next
    
    def parse(self, response):
        impresora = response.xpath("//h2[@class='ui-search-item__title']/text()").extract()
        precio = response.xpath("//span[@class='price-tag-fraction']/text()").extract()

        for item in zip(impresora,precio):
            scraped_info = {
                'Impresora': item[0],
                'Precio': item[1],
            }
            yield scraped_info

    

