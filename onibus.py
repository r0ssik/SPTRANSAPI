import os
import requests
from dotenv import load_dotenv

import folium


load_dotenv("arquivo.env")
x = os.getenv('SPTRANS_TOKEN')
s = requests.Session()
s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={x}"
)
linhas_ramos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Ramos"
)
linhas_ramos = linhas_ramos.json()

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2520"
)
paradas = res.json()
pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2520"
)
bus = pos.json()
busreal = bus['vs']

m = folium.Map(location=[paradas[3]["py"], paradas[3]["px"]], zoom_start=14)

for i in paradas:
    folium.Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)

for i in busreal:
  folium.Marker(location=[i["py"], i["px"]], tooltip="Onibus", icon=folium.Icon(color="green"), ).add_to(m)

m.save("2520.html")
