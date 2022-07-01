import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import json
import glob
import os

### Code used to create a smaller dataset ###
#all_files = glob.glob("data/*.csv")
#
#df = pd.concat((pd.read_csv(f, sep=";")) for f in all_files)
#
#df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
#df_brasil = df[df["regiao"] == "Brasil"]
#
#df_states.to_csv("df_states.csv")
#df_brasil.to_csv("df_brasil.csv")

### 

df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

df_states_ = df_states[df_states["data"]=="2020-05-13"]
brazil_states =json.load(open("geojson/brazil_geo.json", "r"))
df_data = df_states[df_states["estado"]=="RJ"]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox(df_states_,locations="estado",
                            center={"lat":-11.42, "lon":-51.73},
                            color="casosNovos",
                            geojson=brazil_states,
                            color_continuous_scale="Redor",
                            zoom=4,
                            opacity=0.4,
                            hover_data={"casosAcumulado":True, 
                                "casosNovos":True,
                                "obitosNovos": True,
                                "estado":True})

fig2 = go.Figure(layout={"template":"plotly_dark"})
fig2.add_trace(go.Scatter(x=df_data["data"], y=df_data["casosAcumulado"]))
fig2.update_layout(
    paper_bgcolor="#242424",
    plot_bgcolor="#242424",
    autosize=True,
    margin=dict(l=0, r=10,t=10, b=10)
)

#Layout

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="line-graph", figure=fig2)
        ]),
        dbc.Col([
            dcc.Graph(id="choropleth-map", figure=fig)
        ])
    ])
)

fig.update_layout(
    paper_bgcolor="#242424",
    autosize = True,
    mapbox_style = "carto-darkmatter",
    margin = go.Margin(l=0, r=0, t=0, b=0),
    showlegend=False
)

if __name__ == "__main__":
    app.run_server(debug=True)