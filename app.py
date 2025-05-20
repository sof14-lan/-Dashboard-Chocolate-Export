import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV en GitHub
clientes_url = "https://raw.githubusercontent.com/sof14-lan/-Dashboard-Chocolate-Export/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/sof14-lan/-Dashboard-Chocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/sof14-lan/-Dashboard-Chocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/sof14-lan/-Dashboard-Chocolate-Export/main/barreras.csv"

# Cargar los datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título del Dashboard
st.title("🌍 Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país para las tablas
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles de ese país", paises)

# Mostrar datos de clientes (filtrados)
st.subheader("📋 Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones (filtrados)
st.subheader("📦 Exportaciones de Chocolates - Detalle por País")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
st.dataframe(exportaciones_filtradas)

# Mostrar gráfico de exportaciones (NO filtrado)
st.subheader("📊 Exportaciones de Chocolates por País")
fig, ax = plt.subplots()
ax.bar(exportaciones["País"], exportaciones["Exportaciones (USD millones)"], color='#2E86C1')
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title("Exportaciones Totales de Chocolates por País")
plt.xticks(rotation=45)
st.pyplot(fig)

# Mostrar datos de mercados (filtrados)
st.subheader("🏪 Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Mostrar barreras de entrada (filtradas)
st.subheader("🚧 Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis Comparativo de Tamaño de Mercado (NO filtrado)
st.subheader("📈 Comparación de Tamaños de Mercado")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Tamaño del Mercado por País")
plt.xticks(rotation=45)
st.pyplot(fig2)
