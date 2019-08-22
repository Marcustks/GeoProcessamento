import pymongo
from pprint import pprint


client = pymongo.MongoClient(
    "mongodb+srv://sys:marcossales21@cluster-tcc-z3g4b.mongodb.net/test?retryWrites=true&w=majority")
db = client.tcc
collection = db.txt
print('conexão ok')

x= '1'
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

endereco_geral = (str(aux_pais) +","+ str(aux_cep))
print(endereco_geral)

