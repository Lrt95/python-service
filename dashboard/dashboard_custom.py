""" Module dashboard_custom

Created by Antony Correia
Python Docstring
"""

# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from dashboard import dashboard_custom_css as css_custom

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def get_gauge(text):
    """ Function get gauge
     :param text: string title
    :return:
    """
    return go.Figure(go.Indicator(
        mode="gauge+number",
        number={'suffix': " %", 'font': {'size': 50}},
        value=0,
        title={'text': text},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 80], 'color': 'green'},
                {'range': [80, 100], 'color': 'red'}]
        }
    ))


def set_cpu_load_avg(one, five, fifteen):
    """ Function set cpu load avg
        to bar tab
    :param one:
    :param five:
    :param fifteen:
    """
    for i, col in enumerate(fig_cpu_load_avg.data):
        fig_cpu_load_avg.data[i]['y'] = [one, five, fifteen]


def set_cpu_percent(percent):
    """ Function set cpu percent
        to indicator
    :param percent:
    """
    for i, col in enumerate(fig_cpu_percent.data):
        fig_cpu_percent.data[i]['value'] = percent


df_cpu_load_avg = pd.DataFrame({
    "Times": ["1minutes", "5minutes", "15minutes"],
    "Percent": [0, 0, 0]
})
fig_cpu_load_avg = px.bar(df_cpu_load_avg, x="Times", y="Percent", range_y=[0, 100], title="CPU load average")
fig_cpu_percent = get_gauge("CPU Percent")
set_cpu_load_avg(25, 50, 75)
set_cpu_percent(78.52)
fig2 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

app.layout = html.Div(children=[
    html.H1(children='Dash Board Python-Service'),

    html.Div(children='''
        Dash: The best dashboard of the world
    '''),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val'),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit'),
    html.Div(
        style=css_custom.flex_row_space_around,
        children=[
            dcc.Graph(
                id='cpu_load_avg',
                figure=fig_cpu_load_avg
            ),
            dcc.Graph(
                id='cpu_percent',
                figure=fig_cpu_percent
            ),
        ]),
    dcc.Graph(
        id='graph2',
        figure=fig2
    )
])


@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')]
)
def update_output(n_clicks, value):
    return 'The input value was "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
