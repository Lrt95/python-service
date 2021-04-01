""" Module dashboard_custom

Created by Antony Correia
Python Docstring
"""

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from dashboard import dashboard_custom_css as css_custom
from dash.dependencies import Output, Input, State
from dashboard.component_dash import navbar

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
colors = px.colors.qualitative.Plotly


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


def get_graph(title, xaxis_label, yaxis_label, range_yaxis=None):
    """ Function get graph
    :param range_yaxis: list of range y axis
    :param yaxis_label: string label yaxis
    :param xaxis_label: string labels x axis
    :param title: title graph
    :return: Figure graph
    """
    if range_yaxis is None:
        range_yaxis = []
    layout = {
        "layout": {
            "title": title,
            "xaxis_title": xaxis_label,
            "yaxis_title": yaxis_label,
        }
    }
    if range_yaxis:
        layout["layout"]["yaxis"] = {"range": range_yaxis}
    figure = go.Figure(layout)

    return figure


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


def set_cpu_time(cpu_time_user, cpu_time_idle):
    """ Function set cpu time
        to graph
        :param cpu_time_idle:
        :param cpu_time_user:
    """
    times_user = []
    percents_user = []
    times_idle = []
    percents_idle = []
    for time, percent in cpu_time_user:
        times_user.append(time)
        percents_user.append(percent)
    cpu_time_user_dict = {
        'times': times_idle,
        'percents': percents_idle,
        'color': 'cpu_time_user'
    }
    df = pd.DataFrame(cpu_time_user_dict)
    fig_cpu_times.add_traces(
        go.Scatter(name="test", x=df['times'], y=df['percents'], mode='lines', line=dict(color=colors[0])))


df_cpu_load_avg = pd.DataFrame({
    "Times": ["1minutes", "5minutes", "15minutes"],
    "Percent": [0, 0, 0]
})
fig_cpu_load_avg = px.bar(df_cpu_load_avg, x="Times", y="Percent", range_y=[0, 100], title="CPU load average")

fig_cpu_times = get_graph("CPU Times", "Times", "Percent")

# fig_cpu_times.add_traces(
#     go.Scatter(name="test", x=df['times'], y=df['percents'], mode='lines', line=dict(color=colors[0])))


fig_cpu_percent = get_gauge("CPU Percent")
fig_cpu_time_percent_user = get_gauge("CPU Time Percent User")
fig_cpu_time_percent_idle = get_gauge("CPU Time Percent Idle")

set_cpu_load_avg(25, 50, 75)
set_cpu_percent(78.52)
fig2 = go.Figure(data=[go.Scatter(x=[0], y=[0])])

app.layout = html.Div(children=[
    navbar.navbar,
    html.Div(
        style=css_custom.flex_row,
        children=[
            html.H1(children='CPU', style={'margin': '5px'}),
            html.H1(children='', id="h1", style={'margin': '5px'})
        ]),

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
    html.Div(
        style=css_custom.flex_row_space_around,
        children=[
            dcc.Graph(
                id='cpu_time_percent_user',
                figure=fig_cpu_time_percent_user
            ),
            dcc.Graph(
                id='cpu_time_percent_idle',
                figure=fig_cpu_time_percent_idle
            ),
        ]),
    dcc.Graph(
        id='graph2',
        figure=fig2
    ),
    dcc.Graph(
        figure=fig_cpu_times
    )
])


@app.callback(
    Output('h1', 'children'),
    [Input("button_agent", "n_clicks")],
    [State("input_agent", "value")],
)
def app_output(n, value):
    if n:
        print(value)
        return value
    return "Agent"


if __name__ == '__main__':
    app.run_server(debug=True)
