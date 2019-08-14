# coding=utf-8
#Aplicação Python de geocodificação em batch de endereços;
#Este script usa um serviços de geoficador de endereços do ArcGIS e Komoot.
#O projeto precisa um arquivo de entrada csv de modo que funcione corretamente.
#Sua principal funcionalidade é promover um banco de dados de todas as localidades do Brasil com Latitude e longitude

#Marcus Oliveira 01-08-201

import time
import geocoder
import pandas as pd
import requests

# ----------------------------- Entrada de dados -----------------------------#


input_file_path = "input.csv"
output_file_path = "output"


Nome_coluna_endereco = "ENDERECO"
Nome_coluna_cidade = "CIDADE"
Nome_coluna_cep = "CEP"


indice = 0
quantidade = 100
escrita_quantidade = 1000
geocode = 3
espera = 3

# ----------------------------- Leitura do csv -----------------------------#

arquivo = pd.read_csv(input_file_path, low_memory=False)

if Nome_coluna_endereco not in arquivo.columns:
    raise ValueError("Não foi possivel localizar a coluna do endereço.")
if Nome_coluna_cidade not in arquivo.columns:
    raise ValueError("Não foi possivel localizar a coluna da cidade.")

if (Nome_coluna_cep):
    if Nome_coluna_cep not in arquivo.columns:
        raise ValueError("Não foi possivel localizar a coluna de cep.")
    Enderecos = (arquivo[Nome_coluna_endereco] + ', ' + arquivo[Nome_coluna_cep].astype(str) + ', ' + arquivo[Nome_coluna_cidade]).tolist()
else:
    Enderecos = (arquivo[Nome_coluna_endereco] + ', ' + arquivo[Nome_coluna_cidade]).tolist()


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
            encontrar_endereco(endereco, s, tentativa-1, espera+espera)
    return g


# ----- out csv --- #



def Arquivo_saida(data, index):
    Nome_criar_sessao = (output_file_path + str(index) + ".csv")
    print("Criado com sucesso o arquivo de saida " + Nome_criar_sessao)
    aux = pd.DataFrame(data)
    aux.columns = ['Endereco', 'Lat', 'Long', 'Provedor']
    aux.to_csv((Nome_criar_sessao + ".csv"), sep=',', encoding='utf8')


print("Processo terminado com sucesso !")
