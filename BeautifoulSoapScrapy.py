import requests
from bs4 import BeautifulSoup
import re

url = "https://www.premierleague.com/clubs/4/Chelsea/squad"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.content, "html.parser")

### Extraer el  nombre del jugador

jugador_busqueda = soup.find_all("h4",attrs={"name"})
jugadores = []
for i in range(0,len(jugador_busqueda)):
    var=str(jugador_busqueda[i]).split(">")[1].split("<")[0]
    var.replace('"',"")
    jugadores.append(var)

### extraer el enlace
soup = BeautifulSoup(r.content, "html.parser")

soup.find_all('a', href=True)

soup.find_all("u1",class_="squadListContainer squadList block-list-4 block-list-3-m block-list-2-s block-list-padding ",
              href=True)
soup.find("a", {"class": "playerOverviewCard active"})


