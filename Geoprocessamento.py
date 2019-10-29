# coding=utf-8
#Aplicação Python de geocodificação em batch de endereços;
#Este script usa um serviços de geoficador de endereços do ArcGIS e Komoot.
#Sua principal funcionalidade é promover um banco de dados de todas as localidades do Brasil com Latitude e longitude

#Marcus Oliveira 01-08-2019

import time
import geocoder
import pandas as pd
import pymongo
import requests





# ----------------------------- Entrada de dados -----------------------------#


client = pymongo.MongoClient(
    "mongodb+srv://sys:marcossales21@cluster-tcc-z3g4b.mongodb.net/test?retryWrites=true&w=majority")
db = client.tcc
collection = db.txt
print('conexão ok')
x = db.Geoprocessamento.count()
x=x+1

x= str(x)
while True:
 x = str(x)
 endereco = collection.find_one( {"ID": x })
 aux_pais = 'Brasil'
 aux_endereco = endereco['ENDEREÇO']
 aux_municipio = endereco['CIDADE']
 aux_cep = endereco['CEP']
 aux_bairro = endereco['BAIRRO']
 print(aux_cep)
 print(aux_municipio)
 print(aux_endereco)
 print(aux_bairro)

 endereco_geral = (str(aux_pais) +","+ str(aux_cep)+","+str(aux_municipio)+","+str(aux_endereco))
 print(endereco_geral)
 print("--------")


 indice = 0
 quantidade = 10000
 escrita_quantidade = 100000
 geocode = 3
 espera = 3


 Resultado = []
 falhas = 0
 total_falhas = 0

# ----------------------------- Função -----------------------------#


 class GeoSessao:
    def __init__(self):
        self.Arcgis = requests.Session()
        self.Komoot = requests.Session()


 def criar_sessao():
    return GeoSessao()

 def geocode_endereco(endereco, s):
    g = geocoder.arcgis(endereco, session=s.Arcgis)
    if (g.ok == False):
        g = geocoder.komoot(endereco, session=s.Komoot)

    return g


 def encontrar_endereco(endereco, s, tentativa, espera):
    g = geocode_endereco(endereco, s)
    if (g.ok == False):
        time.sleep(espera)
        s = criar_sessao()
        if (tentativa > 0):
            encontrar_endereco(endereco_geral, s, tentativa-1, espera+espera)
    return g


# ----- saida csv --- #
 s = criar_sessao()
 g = encontrar_endereco(endereco_geral, s, geocode, espera)
 print("oque quero")
 print(g)
 print(g.latlng,g.provider)
 aux_lat = g.lat
 aux_lng = g.lng



 geoprocessamento_banco =db.Geoprocessamento

 Geoprocessamento_insert = {
               "_id": x ,
              "Pais": "Brasil",
              "Municipio": aux_municipio ,
              "bairro": aux_bairro ,
              "Endereço": aux_endereco,
              "Cep": aux_cep,
              "Latitude ": aux_lat,
              "longitude": aux_lng,
               "Array_lat_long": g.latlng
             }
 print("insert")
 geoprocessamento_banco.insert_one(Geoprocessamento_insert).inserted_id
 x = int(x)
 x=x+1

 if x == '10':
  break

