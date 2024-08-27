import plotly.express as px
import pandas as pd

# Recebe dados de um banco de dados com veículos hipotéticos e suas localizações
print('getting data....')
df = px.data.carshare()
print(df.head(10))
print(df.tail(10))

# filtra os dados dos carros e transfere para um mapa armazenado em uma variável `fig`.
fig = px.scatter_mapbox(df,
                        lon = df['centroid_lon'], #longitude
                        lat = df['centroid_lat'], #latitude
                        zoom = 3,
                        color = df['peak_hour'], #horario de pico, determina a cor do circulo.
                        size = df['car_hours'], #Quantidade de horas de uso do carro em diferentes locais, determina o tamanho do circulo.
                        width = 1200,
                        height = 900,
                        title = 'Car Share Scatter Map' # Titulo
                        )

# Define o estilo do mapa
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})

# Abre o mapa no seu navegador padrão
fig.show()
print('plot complete.')
