""" Module dashboard_custom

Created by Antony Correia
Python Docstring
"""

from dateutil.parser import parse
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
        "cpu_load_avg_1minutes": data_api[agent]["cpu_load_avg_1minutes"][-1]["value"] * 10,
        "cpu_load_avg_5minutes": data_api[agent]["cpu_load_avg_5minutes"][-1]["value"] * 10,
        "cpu_load_avg_15minutes": data_api[agent]["cpu_load_avg_15minutes"][-1]["value"] * 10
    }


def get_indicator(title, agent, element, time):
    """ Function get indicator
     :param element: string element
     :param agent: string agent
     :param title: string title
    :return:
    """
    data_cpu = get_data_agent_hardware(agent=agent, hardware='cpu', element=element, time=time)
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


def get_graph(title, xaxis_label, yaxis_label, element, time, range_yaxis=None, agent=None):
    """ Function get graph
    :param time: string time
    :param element: string of element
    :param agent: string of agent
    :param range_yaxis: list of range y axis
    :param yaxis_label: string label yaxis
    :param xaxis_label: string labels x axis
    :param title: title graph
    :return: Figure graph
    """
    print(time)
    if range_yaxis is None:
        range_yaxis = []
    if agent is None:
        agent = ""
    data_cpu = get_data_agent_hardware(agent=agent, hardware="cpu", time=time, element=element)
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
                times.append(parse(i['time']).isoformat())
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


def get_pie(agent, elements, total, time):
    labels = []
    values = []
    title = ""
    for element in elements:
        data = get_data_agent_hardware(agent=agent, hardware="memory", time=time, element=element)
        if element != total:
            labels.append(element)
            values.append(data[agent][element][-1]['value'])
        else:
            title = data[agent][element][-1]['value']
    return go.Figure(
        data=[go.Pie(labels=labels, values=values)],
        layout={'title': "Total Memory: " + '{:,.0f}'.format(title / float(1 << 30)) + " GB"}
    )


def get_bar_tab(agent, time):
    """ Function get bar tab
    :return: Bar Tab
    """
    data_cpu = get_data_agent_hardware(agent=agent, hardware="cpu", time=time)
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


def get_text(agent, hardware, element, time):
    data = get_data_agent_hardware(agent=agent, hardware=hardware, element=element, time=time)
    print(type(data[agent][element][-1]['value']))
    return data[agent][element][-1]['value']


def serve_layout():
    """ Function serve layout
    :return: app layout
    """
    return html.Div(children=[
        navbar.navbar,
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='CPU All Users', style={'margin': '5px'})
            ]),
        dcc.Graph(
            id="cpu_time_all_users"
        ),
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='CPU', style={'margin': '5px'}),
                html.H1(children='', id="h1_cpu", style={'margin': '5px'}),
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
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='Memory', style={'margin': '5px'}),
                html.H1(children='', id="h1_memory", style={'margin': '5px'}),
            ]),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                dcc.Graph(id='virtual_memory_total'),
                dcc.Graph(id='virtual_swap_memory')
            ]),
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='Net IO', style={'margin': '5px'}),
                html.H1(children='', id="h1_net", style={'margin': '5px'}),
            ]),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                html.Div(
                    style=css_custom.flex_row,
                    children=[
                        html.Div(
                            children=[
                                html.H1(children='Net IO Counter Bytes', style={'margin': '5px'}),
                                html.H1(children="", id="net_io_counter_bytes_sent", style=css_custom.counter_io),
                                html.H1(children="", id="net_io_counter_bytes_recv", style=css_custom.counter_io)
                            ],
                            style={"margin": "50px"}
                        )
                    ]),
                html.Div(
                    style=css_custom.flex_row,
                    children=[
                        html.Div(
                            children=[
                                html.H1(children='Net IO Counter packets', style={'margin': '5px'}),
                                html.H1(children="", id="net_io_counter_packets_sent", style=css_custom.counter_io),
                                html.H1(children="", id="net_io_counter_packets_recv", style=css_custom.counter_io)
                            ],
                            style={"margin": "50px"}
                        )
                    ]),
            ]
        ),

    ])


app.layout = serve_layout()


@app.callback(
    [
        Output('h1_cpu', 'children'),
        Output('cpu_load_avg', 'figure'),
        Output('cpu_percent', 'figure'),
        Output('cpu_time_percent_user', 'figure'),
        Output('cpu_time_percent_idle', 'figure'),
        Output('h1_memory', 'children'),
        Output('virtual_memory_total', 'figure'),
        Output('virtual_swap_memory', 'figure'),
        Output('select', 'value'),
        Output('cpu_time_all_users', 'figure'),
        Output('h1_net', 'children'),
        Output('net_io_counter_bytes_sent', 'children'),
        Output('net_io_counter_bytes_recv', 'children'),
        Output('net_io_counter_packets_sent', 'children'),
        Output('net_io_counter_packets_recv', 'children'),
    ],
    [Input("button_agent", "n_clicks")],
    [State("input_agent", "value"), State("select", "value")],
)
def app_output(n, value_agent, value_time):
    """Callback app output
    :param value_time: string time
    :param n: click button ok
    :param value_agent: string agent
    :return: component
    """
    default_agent = "Antony"
    default_time = "24h"
    if n:
        return callback_app(value_agent, value_time)
    return callback_app(default_agent, default_time)


def callback_app(agent, time):
    """

    :param agent:
    :param time:
    :return:
    """
    return agent, \
           get_bar_tab(agent, time), \
           get_indicator('CPU Percent', agent, "cpu_percent", time), \
           get_indicator("CPU Time Percent User", agent, "cpu_times_percent_user", time), \
           get_indicator("CPU Time Percent Idle", agent, "cpu_times_percent_idle", time), \
           agent, \
           get_pie(agent,
                   ["virtual_memory_available", "virtual_memory_used", "virtual_memory_total"],
                   "virtual_memory_total", time), \
           get_pie(agent,
                   ["swap_memory_free", "swap_memory_used", "swap_memory_total"],
                   "swap_memory_total", time), \
           time, \
           get_graph("CPU Times Users", "Times", "Percent", "cpu_percent", time=time), \
           agent, \
           'Send: ' '{:,.0f}'.format(
               get_text(agent, "net", "net_io_counters_bytes_sent", time) / float(1 << 30)) + " GB", \
           'Received: ' '{:,.0f}'.format(
               get_text(agent, "net", "net_io_counters_bytes_recv", time) / float(1 << 30)) + " GB", \
           'Send: ' + str(get_text(agent, "net", "net_io_counters_packets_sent", time)) + " packets", \
           'Received: ' + str(get_text(agent, "net", "net_io_counters_packets_recv", time)) + " packets",


if __name__ == '__main__':
    app.run_server(debug=True)
