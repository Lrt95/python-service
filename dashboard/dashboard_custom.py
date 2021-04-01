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
from dashboard.request_api.fetch_data_api import get_data_agent_hardware

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
colors = px.colors.qualitative.Plotly


def get_cpu_load_avg(data_api, agent):
    """ Function get cpu load avg
    :param agent: string agent name
    :param data_api: list data cpu
    :return:
    """
    return {
        "cpu_load_avg_1minutes": data_api[agent]["cpu_load_avg_1minutes"][-1]["value"],
        "cpu_load_avg_5minutes": data_api[agent]["cpu_load_avg_5minutes"][-1]["value"],
        "cpu_load_avg_15minutes": data_api[agent]["cpu_load_avg_15minutes"][-1]["value"]
    }


def get_indicator(title, agent, element):
    """ Function get indicator
     :param element: string element
     :param agent: string agent
     :param title: string title
    :return:
    """
    data_cpu = get_data_agent_hardware(agent=agent, hardware='cpu', element=element, time="24h")
    print(data_cpu[agent][element][-1]["value"])
    indicator = go.Figure(go.Indicator(
        mode="gauge+number",
        number={'suffix': " %", 'font': {'size': 50}},
        value=data_cpu[agent][element][-1]["value"],
        title={'text': title},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 80], 'color': 'green'},
                {'range': [80, 100], 'color': 'red'}]
        }
    ))

    return indicator


def get_graph(title, xaxis_label, yaxis_label, element, range_yaxis=None, agent=None):
    """ Function get graph
    :param element: string of element
    :param agent: string of agent
    :param range_yaxis: list of range y axis
    :param yaxis_label: string label yaxis
    :param xaxis_label: string labels x axis
    :param title: title graph
    :return: Figure graph
    """
    print(element)
    if range_yaxis is None:
        range_yaxis = []
    if agent is None:
        agent = ""
    data_cpu = get_data_agent_hardware(agent=agent, hardware="cpu", time="24h", element=element)
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
    color = 0
    for agent, elements in data_cpu.items():
        times = []
        percents = []
        for element in elements.values():
            for i in element:
                times.append(i["time"])
                percents.append(i["value"])
        cpu_time_user_dict = {
            'times': times,
            'percents': percents
        }
        df = pd.DataFrame(cpu_time_user_dict)
        figure.add_traces(
            go.Scatter(name=agent, x=df['times'], y=df['percents'], mode='lines', line=dict(color=colors[color])))
        color += 1
    return figure


def get_graph2(title, xaxis_label, yaxis_label, element, range_yaxis=None, agent=None):
    """ Function get graph
    :param element: string of element
    :param agent: string of agent
    :param range_yaxis: list of range y axis
    :param yaxis_label: string label yaxis
    :param xaxis_label: string labels x axis
    :param title: title graph
    :return: Figure graph
    """
    print(element)
    if range_yaxis is None:
        range_yaxis = []
    if agent is None:
        agent = ""
    # data_cpu = get_data_agent_hardware(agent=agent, hardware="cpu", time="24h", element=element)
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
    color = 0
    times_1 = [0, 2, 3, 4]
    percents_1 = [10, 20, 10, 20]
    times_2 = [1, 4, 2, 4]
    percents_2 = [30, 60, 10, 40]
    # for agent, elements in data_cpu.items():
    #     times = []
    #     percents = []
    #     for element in elements.values():
    #         for i in element:
    #             times.append(i["time"])
    #             percents.append(i["value"])
    cpu_time_user_dict = {
        'times': times_1,
        'percents': percents_1
    }
    df2 = pd.DataFrame(cpu_time_user_dict)
    cpu_time_user_dict2 = {
        'times': times_2,
        'percents': percents_2
    }
    df = pd.DataFrame(cpu_time_user_dict)
    df2 = pd.DataFrame(cpu_time_user_dict2)
    figure.add_traces(
        go.Scatter(name="agent", x=df['times'], y=df['percents'], mode='lines', line=dict(color=colors[0])))
    figure.add_traces(
        go.Scatter(name="agent2", x=df2['times'], y=df2['percents'], mode='lines', line=dict(color=colors[1])))
    color += 1
    return figure


def get_bar_tab(agent):
    """ Function get bar tab
    :return: Bar Tab
    """
    data_cpu = get_data_agent_hardware(agent, "cpu", "24h")
    cpu_load_avg = get_cpu_load_avg(data_cpu, agent)
    df_cpu_load_avg = pd.DataFrame({
        "Times": ["1minutes", "5minutes", "15minutes"],
        "Percent": [0, 0, 0]
    })
    bar_tab = px.bar(df_cpu_load_avg, x="Times", y="Percent", title="CPU load average")
    for i, col in enumerate(bar_tab.data):
        bar_tab.data[i]['y'] = [
            cpu_load_avg["cpu_load_avg_1minutes"],
            cpu_load_avg["cpu_load_avg_5minutes"],
            cpu_load_avg["cpu_load_avg_15minutes"]
        ]
    return bar_tab


fig_cpu_times = get_graph("CPU Times Users", "Times", "Percent", "cpu_times_percent_user")

fig_test = get_graph2("CPU Times Users", "Times", "Percent", "cpu_times_percent_user")

def serve_layout():
    return html.Div(children=[
        navbar.navbar,
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='CPU', style={'margin': '5px'}),
                html.H1(children='', id="h1", style={'margin': '5px'}),
            ]),

        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                dcc.Graph(id='cpu_load_avg'),
                dcc.Graph(id='cpu_percent'),
            ]),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                dcc.Graph(id='cpu_time_percent_user'),
                dcc.Graph(id='cpu_time_percent_idle'),
            ]),
        dcc.Graph(
            figure=fig_cpu_times
        ),
        dcc.Graph(
            figure=fig_test
        )
    ])


app.layout = serve_layout()


@app.callback(
    [
        Output('h1', 'children'),
        Output('cpu_load_avg', 'figure'),
        Output('cpu_percent', 'figure'),
        Output('cpu_time_percent_user', 'figure'),
        Output('cpu_time_percent_idle', 'figure')
    ],
    [Input("button_agent", "n_clicks")],
    [State("input_agent", "value")],
)
def app_output(n, value):
    """Callback app output
    :param n: click button ok
    :param value: string agent
    :return: component
    """
    if n:
        return value, get_bar_tab(value), \
               get_indicator('CPU Percent', value, "cpu_percent"), \
               get_indicator("CPU Time Percent User", value, "cpu_times_percent_user"), \
               get_indicator("CPU Time Percent Idle", value, "cpu_times_percent_idle")
    return "agent0", get_bar_tab("agent0"), \
           get_indicator('CPU Percent', "agent0", "cpu_percent"), \
           get_indicator("CPU Time Percent User", 'agent0', "cpu_times_percent_user"), \
           get_indicator("CPU Time Percent Idle", 'agent0', "cpu_times_percent_idle")


if __name__ == '__main__':
    app.run_server(debug=True)
