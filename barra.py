import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")


# Agrupar e ordenar os dados
df_agrupado = df.groupby("Marca")["Qtd_Vendidos_Cod"].sum().reset_index()
df_agrupado = df_agrupado.sort_values(by="Qtd_Vendidos_Cod", ascending=False)  # Ordenar do maior para o menor
df_top20 = df_agrupado.head(20)  # Pega apenas as 20 marcas mais vendidas
# Criar o gráfico de barras
plt.figure(figsize=(15, 6))  # Ajustar tamanho para caber as 108 marcas
sns.barplot(data=df_top20, x="Marca", y="Qtd_Vendidos_Cod", palette="viridis")
# Melhorias na visualização
plt.xticks(rotation=90, ha="right", fontsize=8)  # Rotacionar os rótulos para melhor leitura
plt.xlabel("Marca")
plt.ylabel("Quantidade de Vendas")
plt.title(" Marcas mais Vendidas")
plt.grid(axis="y", linestyle="--", alpha=0.5)  # Adicionar grid no eixo Y
plt.tight_layout()  # Ajustar layout automaticamente

# Exibir o gráfico
plt.show()



# Agrupar e ordenar os dados
df_agrupado = df.groupby("Temporada")["Qtd_Vendidos_Cod"].sum().reset_index()
df_agrupado = df_agrupado.sort_values(by="Qtd_Vendidos_Cod", ascending=False)  # Ordenar do maior para o menor
# Criar o gráfico de barras
plt.figure(figsize=(15, 6))  # Ajustar tamanho para caber as 108 marcas
sns.barplot(data=df_agrupado, x="Temporada", y="Qtd_Vendidos_Cod", palette="viridis")
# Melhorias na visualização
plt.xticks(rotation=45, ha="right", fontsize=8)  # Rotacionar os rótulos para melhor leitura
plt.xlabel(" Temporada ")
plt.ylabel("Quantidade de Vendas")
plt.title("Quantidade de Vendas por Temporada")
plt.grid(axis="y", linestyle="--", alpha=0.5)  # Adicionar grid no eixo Y
plt.tight_layout()  # Ajustar layout automaticamente
# Exibir o gráfico
plt.show()



