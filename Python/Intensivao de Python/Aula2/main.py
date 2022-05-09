import pandas as pd
import plotly.express as px

# IMPORTAR O ARQUIVO
tabela = pd.read_csv("Materiais/telecom_users.csv")

# REMOVER COLUNAS QUE NÃO VAO AJUDAR
tabela = tabela.drop("Unnamed: 0", axis=1)
# axis = 0 -> Linha
# axis = 1 -> Coluna

# ANALIZAR SE O PYTHON ESTA LENDO AS INFORMAÇOES NO FORMATO CORRETO
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# print(tabela.info())

# EXCLUIR COLUNAS COMPLETAMENTE VAZIAS
tabela = tabela.dropna(how="all", axis=1)

# EXCLUIR LINHAS COMPLETAMENTE VAZIAS
tabela = tabela.dropna(how="any", axis=0)


# QUANTOS CLIENTES CANCELARAM E QUANTOS NÃO CANCELARAM
print(tabela["Churn"].value_counts())

# O %(PERCENTUAL) DE CLIENTES QUE CANCELARAM E QUE NÃO CANCELARAM
print(tabela["Churn"].value_counts(normalize=True).map("{:.200%}".format))


# --------------------------------------------------GRAFICO--------------------------------------------------
for coluna in tabela.columns:
        
    # coluna = "MesesComoCliente"

    # CRIAR O GRAFICO
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    # EXIBIR O GRAFICO
    grafico.show()
