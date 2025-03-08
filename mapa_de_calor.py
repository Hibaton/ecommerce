import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# DataFrame usado para correlacao
df_corr=df[['Preço','Nota_MinMax','N_Avaliações_MinMax','Desconto_MinMax','Qtd_Vendidos_Cod']].corr()
# renomear os nomes das colunas
df_renomeado = df_corr.rename(columns={
    "Preco": "Preço",
    "Nota_MinMax": "Nota Normalizada",
    "N_Avaliações_MinMax": "Avaliações",
    "Desconto_MinMax": "Desconto",
    "Qtd_Vendidos_Cod": "Qtd Vendidos"
}, index={
    "Preco": "Preço",
    "Nota_MinMax": "Nota Normalizada",
    "N_Avaliações_MinMax": "Avaliações",
    "Desconto_MinMax": "Desconto",
    "Qtd_Vendidos_Cod": "Qtd Vendidos"
})

# Heatmap de correlacao com os novos nomes
plt.figure(figsize=(10,6))
sns.heatmap(df_renomeado, annot=True, fmt=".2f")
plt.title('Mapa de Calor de Correlação entre Variáveis')
# Ajusta automaticamente o layout para evitar cortes
plt.tight_layout()
plt.show()