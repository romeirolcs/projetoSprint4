# Bibliotecas

import pandas as pd
import plotly_express as px
import streamlit as st

# Dataset principal

car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho

st.header('Análise de informações sobre Anúncios de vendas de carros')

# Botão para Histograma

hist_button = st.button('Criar histograma')
        
if hist_button:
            
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
                
            fig = px.histogram(car_data, x="odometer")
        
            st.plotly_chart(fig, use_container_width=True)

# Botão para Gráfico de Dispersão

hist_button = st.button('Criar gráfico de dispersão')
        
if hist_button:
            
            st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
                
            fig = px.scatter(car_data, x="odometer", y="price")
        
            fig.show()