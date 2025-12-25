import pandas as pd 
import plotly.express as px
import streamlit as st

st.header('Análisis de Vehículos Usados')

car_data = pd.read_csv('vehicles_us.csv')

# Crear botón para histograma
hist_button = st.button('Pulsa el boton para construir el histograma')

if hist_button:
    st.write('Espera mientras se crea el histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear botón para gráfico de dispersión  
scatter_button = st.button('Pulsa el boton para construir el grafico de dispersion')

if scatter_button:
    st.write('Espera mientras se crea el gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)