
#Marcus Oliveira 



import pandas as pd



# ----------------------------- Variaveis ------------------------------------#




# ----------------------------- Entrada de dados -----------------------------#


input_file_path = "input.csv"
 


Nome_coluna_endereco = "ENDERECO"
Nome_coluna_cidade = "CIDADE"
Nome_coluna_cep = "CEP"   


# ----------------------------- Leitura do csv -----------------------------#

#leitura
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