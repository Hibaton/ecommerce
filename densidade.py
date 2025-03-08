import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# Grafico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
# Adicionar rótulos e título
plt.title('Densidade das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Densidade')
plt.show()

