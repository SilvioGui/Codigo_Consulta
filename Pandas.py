Os principais comandos do pandas incluem:

#pd.read_csv(): ler um arquivo CSV e retornar um DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

#df.head(): mostrar as primeiras linhas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

#df.tail(): mostrar as últimas linhas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.tail())

#df.shape: mostrar o número de linhas e colunas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.shape)

#df.columns: mostrar o nome das colunas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.columns)

#df.info(): mostrar informações gerais sobre o DataFrame, incluindo o número de linhas, número de colunas, tipos de dados e uso de memória
import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

#df.describe(): mostrar estatísticas gerais sobre as colunas numéricas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
print(df.describe())

#df.sort_values(): ordenar um DataFrame por uma ou mais colunas
import pandas as pd

df = pd.read_csv('data.csv')
df = df.sort_values('column_name')

#df.set_index(): definir uma coluna como o índice de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
df = df.set_index('column_name')

#df.loc[]: acessar linhas de um DataFrame usando rótulos
import pandas as pd

df = pd.read_csv('data.csv')
print(df.loc[0])

#df.iloc[]: acessar linhas de um DataFrame usando posições inteiras
import pandas as pd

df = pd.read_csv('data.csv')
print(df.iloc[0])

#df.query(): filtrar linhas de um DataFrame usando uma expressão lógica
import pandas as pd

df = pd.read_csv('data.csv')
print(df.query('column_name > value'))

#df.groupby(): agrupar linhas de um DataFrame por valores em uma ou mais colunas
import pandas as pd

df = pd.read_csv('data.csv')
grouped = df.groupby('column_name')
print(grouped.mean())

#df.pivot_table(): criar uma tabela dinâmica (raspagem) a partir de um DataFrame.
import pandas as pd

df = pd.read_csv('data.csv')
pivot_table = df.pivot_table(values='column_name', index='column_name', columns='column_name')

#df.apply(): aplicar uma função em uma ou mais colunas de um DataFrame
import pandas as pd

df = pd.read_csv('data.csv')
def custom_func(x):
return x*2

df['new_column'] = df['column_name'].apply(custom_func)

