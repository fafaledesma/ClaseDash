import dash
from dash import dcc
from dash import html

import plotly.graph_objects as go

import numpy as np

from ClaseDash.graph import *

def create_scatter_plot_1():
    np.random.seed(42)
    random_x= np.random.randint(0,101,100)
    random_y= np.random.randint(0,101,100)

    data= [go.Scatter(x=random_x, y=random_y, mode='markers', name='Random Data')]
    layout=go.Layout(title='My graph on dash')

    return go.Figure(data=data, layout=layout)
    

app = dash.Dash()


app.layout = html.Div([
    html.H1("Hola Dash!"),
    html.Hr(),
    html.H3("Mi primera app en Dash"),
    html.P("Esta es la primera ocasión en que estoy modificando mi página web"),
    dcc.Graph(
        id = 'graph_1',
        figure=create_scatter_plot_1()
    ),
    dcc.Graph(
        id = 'graph_2',
        figure=create_line_plot()
    ),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ]),
    html.H5("Lista sin numeros"),
    html.Ul([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    html.H5("Lista enumerada"),
    html.Ol([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    ])

if __name__ == '_main_':
    app.run_server()

    app.layout = html.Div([
    html.H1("Hola Dash!"),
    html.H3("Mi primera app de Dash"),
    html.P("Esta es la muestra de una aplicacion de dash, no hemos creado gráficos pero estamos poniendo información"),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ])
    ])

if __name__ == "__main__":
    app.run_server()