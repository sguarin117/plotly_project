import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
scatterplot_button = st.button(
    'Construir diagrama de dispersion')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scatterplot_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersion odómetro vs. precio')

    # crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x="odometer",
                             y="price", opacity=0.7, height=500)
    st.plotly_chart(scatter_fig, use_container_width=True)
