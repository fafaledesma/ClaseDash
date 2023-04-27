import numpy as np
import plotly.graph_objects as go

def create_scatter_plot_1():
    
    np.random.seed(42)

    random_x = np.random.randint(0,101,100)
    random_y = np.random.randint(0,101,100)

    data = [go.Scatter(x=random_x,y=random_y,mode='markers',name='Random Data')]

    layout = go.Layout(title='My graph on Dash')

    return go.Figure(data=data,layout=layout)

def create_line_plot():
    np.random.seed(56)

    x_values= np.linspace(0,1,100)
    y_values = np.random.randn(100)

    trace0 = go.Scatter(x=x_values,y=y_values+5,mode='markers',name='markers')
    trace1 = go.Scatter(x=x_values,y=y_values,mode='lines',name='lines')
    trace2 = go.Scatter(x=x_values,y=y_values-5,mode='lines+markers',name='lined & markers')

    data = [trace0, trace1, trace2]

    layout = go.Layout(title='Line Charts')

    fig = go.Figure(data=data,layout=layout)
    return fig