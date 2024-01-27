from server import server
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from flask import Flask, jsonify
from app import server

@server.route('/api/data', methods=['GET'])
def get_data():
    # Your code to fetch and return data
    return jsonify({'data': 'Your data'})

data = {
    'year': [1000, 1200, 1400, 1600, 1800, 2000],
    'empires': [10, 15, 20, 18, 25, 30],
    'major_battles': [5, 8, 12, 20, 25, 30]
}

df = pd.DataFrame(data)

app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    dcc.Graph(id='map-visualization'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
    html.Div(id='slider-output-container')
])

@app.callback(
    Output('map-visualization', 'figure'),
    [Input('year-slider', 'value')]
)
def update_map(selected_year):
    
    data = [
        go.Scattergeo(
            lon=[-74, -20, 50],
            lat=[40.7, 47, 30],
            mode='markers',
            marker=dict(size=10, color='rgb(255,0,0)')
        )
    ]

    layout = go.Layout(
        title='Map Visualization',
        geo=dict(
            projection=dict(type='mercator'),
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)'
        )
    )

    return {'data': data, 'layout': layout}

@app.callback(
    Output('slider-output-container', 'children'),
    [Input('year-slider', 'value')]
)
def update_output(value):
    return 'Selected Year: {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)