import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# Grafico de regressao
sns.regplot(x='N_Avaliações', y='Qtd_Vendidos_Cod', data=df,color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
# Adicionar rótulos e título
plt.title('Regressao de Avaliações por Quantidade Vendida ')
plt.xlabel('Numero de Avaliações ')
plt.ylabel('Quantidade Vendida')
# Exibir o gráfico
plt.show()
