# Scrapy-Mercado
Código rápido para descargar Data de Mercado Libre

Este código es una representación sencilla de descargar el titulo de una impresora y el precio de la pagina de mercado libre usando **Scrapy**  además, agrega el uso del pipeline 
para exportar el archivo en la carpeta del proyecto y también, incluye el cambio del **delimitador** en el pipeline

Descargue el archivo mercadolibre.zip

Para ejecutar la araña, en Anaconda promtp siga lo siguiente:
1. cd mercadolibre
2. scrapy crawl mercado
3. Revise el archivo generado en la carpeta mercadolibre

En start_urls, el parametro range solo se hace para que solo scrapee las dos primeras listas de impresar en mercado libre

El proyecto Book, es tomado de https://medium.com/quick-code/python-scrapy-tutorial-for-beginners-04-crawler-rules-and-linkextractor-7a79aeb8d72

