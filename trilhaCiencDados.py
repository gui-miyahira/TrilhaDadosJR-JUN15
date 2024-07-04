#--Importando a biblioteca panda
import pandas as pd 


#--Inserindo os dados do arquivo CSV
tabela = pd.read_csv("texto.csv", sep=",")


#--Exibindo as primeiras linhas do conjunto de dados;
#--número de linhas
#--número de colunas
#--tipos de dados da tabela


print("\nPrimeiras 5 linhas do DataFrame: \n")
print(tabela.head())

print("\nNúmero de linhas:", tabela.shape[0])


print("\nNúmero de colunas:", tabela.shape[1])


print("\nTipos de dados da tabela:\n")
print(tabela.dtypes,"\n")


