import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# Criar o histograma das precos
plt.figure(figsize=(10,6))
plt.hist(df['Preço'],bins=50,color='green',alpha=0.8)
# Adicionar rótulos e título
plt.title('Distribuição de Preço')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.xticks(ticks=range(0, int(df['Preço'].max())+20, 20))  # Tenta exibir 20 marcações no eixo X
# Mostrar o gráfico
plt.show()



# Criar o histograma das notas
plt.hist(df['Nota'], bins=10, edgecolor='black', color='skyblue')
# Adicionar rótulos e título
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.title('Distribuição das Notas dos Produtos')
# Mostrar o gráfico
plt.show()