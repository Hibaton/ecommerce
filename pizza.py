import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ler os dados no DataFrame
df = pd.read_csv(r"C:\Users\moha_\Downloads\ecommerce_estatistica.csv")

# Selecionar os 2 Generos mais vendidas e agrupar o restante em "Outros"
top_n=2
df_agrupado = df.groupby("Gênero")["Qtd_Vendidos_Cod"].sum().reset_index()
df_agrupado = df_agrupado.sort_values(by="Qtd_Vendidos_Cod", ascending=False)  # Ordenar do maior para
df_top = df_agrupado.head(2)  # Pega apenas as 2 generos mais vendidas
df_outras = pd.DataFrame({'Gênero': ['Outros'], 'Qtd_Vendidos_Cod': [df_agrupado.iloc[top_n:]['Qtd_Vendidos_Cod'].sum()]})
# Concatenar os dados
df_final = pd.concat([df_top, df_outras])
# Grafico de pizza
plt.figure(figsize=(8,6))
plt.pie(df_final['Qtd_Vendidos_Cod'],
        labels=df_final["Gênero"],
        autopct=lambda p: f'{p:.1f}%',  # Formata as porcentagens com 1 casa decimal
        startangle=140,
        colors=plt.cm.Paired.colors,
        shadow=True,
        textprops={'fontsize': 12, 'weight': 'bold'},  # Ajusta fonte dos textos
        wedgeprops={'edgecolor': 'black', 'linewidth': 1},  # Adiciona bordas pretas para melhor contraste
        pctdistance=0.8,  # Afasta os percentuais do centro
        labeldistance=1.1)  # Afasta os rótulos das categorias


# plt.pie(df_final["Qtd_Vendidos_Cod"], labels=df_final["Gênero"], autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição de Vendas por Gênero')
plt.show()





# Remover duplicatas para obter valores únicos por marca
df_unico = df[["Marca", "Marca_Freq"]].drop_duplicates()

# Selecionar as 10 marcas mais registradas
df_top20 = df_unico.nlargest(20, "Marca_Freq")

# Criar gráfico de pizza
plt.figure(figsize=(8, 8))
cores = plt.cm.Paired.colors  # Paleta de cores
explode = [0.05] * len(df_top20)  # Destacar fatias levemente
plt.pie(
    df_top20["Marca_Freq"],  # Valores numéricos que definem o tamanho de cada fatia
    labels=df_top20["Marca"],  # Rótulos para cada fatia (nomes das marcas)
    autopct=lambda p: f'{p:.1f}%',  # Formata os percentuais com uma casa decimal
    startangle=140,  # Ângulo inicial para a primeira fatia (140 graus)
    colors=cores,  # Lista de cores para cada fatia
    explode=explode,  # Destaca fatias
    shadow=True,  # Adiciona sombra ao gráfico para efeito 3D
    textprops={'fontsize': 12, 'weight': 'bold'},  # Propriedades do texto
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},  # Propriedades das bordas das fatias (cor e espessura)
    pctdistance=0.8,  # Distância dos percentuais em relação ao centro (80% do raio)
    labeldistance=1.1  # Distância dos rótulos em relação ao centro (110% do raio)
)
# Adicionar título
plt.title(" Marcas Mais Registradas", fontsize=14, weight="bold")

# Exibir gráfico
plt.show()
