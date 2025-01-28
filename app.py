import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('sales_data.csv')

print("Primeiras linhas dos dados:")
print(data.head())

print("\nNomes das colunas:")
print(data.columns)

data.columns=data.columns.str.strip()

print("\nEstatísticas Descritivas:")
print(data.describe())

vendas_por_produto=data.groupby('Produto')['Vendas'].sum()
print("\nVendas totais por produto:")
print(vendas_por_produto)

vendas_por_produto.plot(kind='bar', color='skyblue', title='Vendas totais por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data['Data']=pd.to_datetime(data['Data'], errors='coerce')
data.sort_values('Data', inplace=True)

vendas_por_data=data.groupby('Data')['Vendas'].sum()
vendas_por_data.plot(kind='line', color='orange', marker='o', title='Vendas ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Total de vendas')
plt.tight_layout()
plt.show()
