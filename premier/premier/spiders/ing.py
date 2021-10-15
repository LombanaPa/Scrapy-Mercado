import scrapy
from premier.items import PremierItem
import numpy as np
import pandas as pd
from datetime import datetime

class IngSpider(scrapy.Spider):
    name = 'ing'
    allowed_domains = ['www.premierleague.com']
    start_urls = ['http://www.premierleague.com/tables']
    
    def parse(self, response):
       
        team = response.xpath("//span[@class='long']/text()").extract()
        played=[]
        won = []
        drawn=[]
        lost = []
        gf = []
        gc = []
        gd = []
        points = []
        ### Extraer campos como equipo, partidos jugados, puntos y demás

        for j in np.arange(4,12,1):
            for i in np.arange(1,41,2):
                if j==4:
                    played.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==5:
                    won.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==6:
                    drawn.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==7:
                    lost.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==8:
                    gf.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==9:
                    gc.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])
                elif j==10:
                    gd.append(response.xpath('normalize-space(//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text())'.format(i,j))\
                        .extract()[0])
                elif j==11:
                    points.append(response.xpath('//*[@id="mainContent"]/div[2]/div[5]/div/div/div/table/tbody/tr[{0}]/td[{1}]/text()'.format(i,j))\
                        .extract()[0])

        ### Extraer resultados de los últimos 5 partidos


        forma = np.array(response.xpath('//*[@id="Tooltip"]/abbr/text()').extract()).reshape(-1,5)[0:20]

        forma1 = []
        forma2 = []
        forma3 = []
        forma4 = []
        forma5 = []


        for form in np.arange(0,20,1):
            forma1.append(forma[form][0])
            forma2.append(forma[form][1])
            forma3.append(forma[form][2])
            forma4.append(forma[form][3])
            forma5.append(forma[form][4])
        

        ### Traer la fecha de los partidos jugados
        fecha = np.array(response.xpath("//span[@class='matchInfo']/text()").extract())[0:310].reshape(-1,5)[0:20]

        fecha1 = []
        fecha2 = []
        fecha3 = []
        fecha4 = []
        fecha5 = []


        for fec in np.arange(0,20,1):
            fecha1.append(fecha[fec][0])
            fecha2.append(fecha[fec][1])
            fecha3.append(fecha[fec][2])
            fecha4.append(fecha[fec][3])
            fecha5.append(fecha[fec][4])

        ### Partidos jugados //div[@class="matchAbridged"]/span[@class='teamName']

        rivales = np.array(response.xpath('//div[@class="matchAbridged"]/span[@class="teamName"]/abbr/@title').extract()[0:240]).reshape(-1,12)

        rival1 = []
        rival2 = []
        rival3 = []
        rival4 = []
        rival5 = []
        Proximo= []
        Equipo_info = []

        def EquipoUnico(df):
            (unique, counts) = np.unique(df,return_counts=True)

            frecuencias = dict(np.asarray([unique, counts]).T)

            df_conteo = pd.DataFrame(frecuencias.items()
                                        , columns=['Equipo', 'Count']).sort_values(by='Count', ascending=False,
                                                                                ).reset_index(drop=True)
            return df,df_conteo.iloc[0]['Equipo']


        def Duplas(df2):
            dupla_equipo = []
            inicio = 0
            fin = 1
            for i in np.arange(0,6,1):
                dupla_equipo.append(df2[inicio] + " vs " + df2[fin])
                inicio +=2
                fin +=2
            return dupla_equipo
        
        for riv in np.arange(0,20,1):
            contrincante,Equipo= EquipoUnico(rivales[riv])
            partidos_pasados = Duplas(rivales[riv])
            rival1.append(partidos_pasados[0])
            rival2.append(partidos_pasados[1])
            rival3.append(partidos_pasados[2])
            rival4.append(partidos_pasados[3])
            rival5.append(partidos_pasados[4])
            Proximo.append(partidos_pasados[5])
            Equipo_info.append(Equipo)

        ### Adjuntar todos los resultados

        for item in zip(team,played,won,drawn,lost,gf,gc,gd,points,forma1,forma2,forma3,forma4,forma5,
        fecha1,fecha2,fecha3,fecha4,fecha5,rival1,rival2,rival3,rival4,rival5,Proximo,Equipo_info):
            premier_table = {
                'FechaScrapy': str(datetime.today())[0:10],
                'Team':item[0],
                'Played':item[1],
                'Win':item[2],
                'Draw':item[3],
                'Lost':item[4],
                'Gf':item[5],
                'Gc':item[6],
                'Gd':item[7],
                'Points':item[8],
                'Partido1':item[9],
                'Partido2':item[10],
                'Partido3':item[11],
                'Partido4':item[12],
                'Partido5':item[13],
                'Fecha1':item[14],
                'Fecha2':item[15],
                'Fecha3':item[16],
                'Fecha4':item[17],
                'Fecha5':item[18],
                'Rival1':item[19],
                'Rival2':item[20],
                'Rival3':item[21],
                'Rival4':item[22],
                'Rival5':item[23],
                'ProximoPartido':item[24],
                'EquipoInfo':item[25]
                            }
            yield premier_table




