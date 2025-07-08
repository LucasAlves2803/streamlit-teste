import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vendas por Cliente")

# Carrega a planilha
df = pd.read_excel("Planilha_Base_Grafico.xlsx", sheet_name="Base")

# Filtro de cliente
clientes = df["Cliente"].unique()
cliente = st.selectbox("Selecione um cliente:", clientes)

# Filtrar dados
df_cliente = df[df["Cliente"] == cliente]

# Exibir dados
st.write(f"Dados de vendas para {cliente}")
st.dataframe(df_cliente)

# Gráfico de barras
fig = px.bar(df_cliente, x="Mês", y="Vendas", title=f"Vendas mensais de {cliente}")
st.plotly_chart(fig)
