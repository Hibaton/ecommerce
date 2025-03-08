import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# Criar o grafico de Dispersao das notas
plt.figure(figsize=(10,6))
plt.scatter(df['Desconto'], df['Qtd_Vendidos_Cod'], color='blue', alpha=0.5)
# Adicionar rótulos e título
plt.title('Dispersão de Preço vs Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')

plt.grid(True)
# Mostrar o gráfico
plt.show()



