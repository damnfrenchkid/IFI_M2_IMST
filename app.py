from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import folium
import altair
from dash.dependencies import Input, Output, State


# Initialisation de l'application Dash
app = Dash(__name__,
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
app.title = "IFI en France"
server = app.server

# Importation des fichiers Excel en utilisant Pandas
df_2019 = pd.read_excel("IFIrégions2019.xlsx")
df_2020 = pd.read_excel("IFIrégions2020.xlsx")
df_2021 = pd.read_excel("IFIrégions2021.xlsx")

# Concaténation des données des trois années
df = pd.concat([df_2019, df_2020, df_2021])
geofrance = "regions.geojson"

# Créer un choropleth pour 2019 en utilisant la colonne patrimoine_moyen
m_2019 = folium.Map(location=[46.2276, 2.2137], zoom_start=6)
folium.Choropleth(
    geo_data=geofrance,
    data=df_2019,
    name='patrimoine2019',
    columns=["Régions","Moyenne du Patrimoine moyen en 2019 par régions (en millions d'€)"],
    key_on="properties.nom",
    fill_color="YlOrBr",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name="Patrimoine moyen (en €) - 2019",
    highlight=True,
    bins=20
).add_to(m_2019)

# Créer un choropleth pour 2020 en utilisant la colonne patrimoine_moyen
m_2020 = folium.Map(location=[46.2276, 2.2137], zoom_start=6)
folium.Choropleth(
    geo_data=geofrance,
    data=df_2020,
    name='patrimoine2020',
    columns=["Régions","Moyenne du Patrimoine moyen en 2020 par régions (en millions d'€)"],
    key_on="properties.nom",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name="Patrimoine moyen (en €) - 2020",
    highlight=True,
    bins=20
).add_to(m_2020)

# Créer un choropleth pour 2021 en utilisant la colonne patrimoine_moyen
m_2021 = folium.Map(location=[46.2276, 2.2137], zoom_start=6)
folium.Choropleth(
    geo_data=geofrance,
    data=df_2021,
    name='patrimoine2021',
    columns=["Régions","Moyenne du Patrimoine moyen en 2021 par régions (en millions d'€)"],
    key_on="properties.nom",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name="Patrimoine moyen (en €) - 2020",
    highlight=True,
    bins=20
).add_to(m_2021)

app.layout = html.Div([
    html.H1("Cartes des régions"),
    dcc.Tabs(id="tabs", value="tab-1", children=[
        dcc.Tab(label="2019", value="tab-1", children=[
            html.Iframe(srcDoc=m_2019._repr_html_(),
                        width="100%", height="1000")
        ]),
        dcc.Tab(label="2020", value="tab-2", children=[
            html.Iframe(srcDoc=m_2020._repr_html_(),
                        width="100%", height="1000")
        ]),
        dcc.Tab(label="2021", value="tab-3", children=[
            html.Iframe(srcDoc=m_2021._repr_html_(),
                        width="100%", height="1000")
        ]),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
