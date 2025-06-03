import streamlit as st
import pandas as pd
import plotly_express as px
#leer archivo
car_data = pd.read_csv('Notebooks/vehicles_us.csv')

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

# Casilla para diagrama de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión: odómetro vs precio')
if build_scatter:
    st.write('Gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig, use_container_width=True)