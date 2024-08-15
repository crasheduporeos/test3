import pandas as pd
import numpy as np
import plotly.express as px
import dash_auth

from dash import Dash, dcc, html, Input, Output


np.random.randint(100,800,20)
names = ["Cola", "Sprite"]
start_date = '2007'
date_range = pd.date_range(start=start_date, periods=20, freq='Y').year
df = pd.DataFrame([np.random.randint(100,800,40), names*20, [year for year in date_range for i in range(2)]])
df = df.transpose()
df.rename(columns = {0:"Value", 1:"Brand", 2:"Year"}, inplace = True)

VALID_USERNAME_PASSWORD_PAIRS = {"login" : "password"}


app = Dash(__name__)
server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)




app.layout = html.Div([
    html.H1("Data of carbonated drinks"),
    dcc.Dropdown(options=[year for year in df.Year.unique()], value=2015, id="choose-year"),
    dcc.Graph(figure=px.bar(df, x="Brand", y="Value"), id="value_to_shw")
])


@app.callback(
    Output(component_id='value_to_shw', component_property='figure'),
    Input(component_id='choose-year', component_property='value')

)
def update_graph(year):
    fig = px.bar(df[df["Year"] == year], x="Brand", y="Value")
    return fig


if __name__ == "__main__":
    app.run_server(debug=False, port = 8040)
