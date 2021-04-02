""" Module dashboard_custom

Created by Antony Correia
Python Docstring
"""

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dashboard import dashboard_custom_css as css_custom
from dash.dependencies import Output, Input, State
from dashboard.component_dash import navbar
from dashboard.component_dash.figure_custom import get_bar_tab, get_indicator, get_pie, get_graph, get_text

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


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
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='Disk IO', style={'margin': '5px'}),
                html.H1(children='', id="h1_disk", style={'margin': '5px'}),
            ]),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                html.Div(
                    style=css_custom.flex_row,
                    children=[
                        html.Div(
                            children=[
                                html.H1(children='Disk IO Counter Bytes', style={'margin': '5px'}),
                                html.H1(children="", id="disk_io_counter_bytes_read", style=css_custom.counter_io),
                                html.H1(children="", id="disk_io_counter_bytes_write", style=css_custom.counter_io)
                            ],
                            style={"margin": "50px"}
                        )
                    ]),
                html.Div(
                    style=css_custom.flex_row,
                    children=[
                        html.Div(
                            children=[
                                html.H1(children='Disk IO Counter', style={'margin': '5px'}),
                                html.H1(children="", id="disk_io_counter_read", style=css_custom.counter_io),
                                html.H1(children="", id="disk_io_counter_write", style=css_custom.counter_io)
                            ],
                            style={"margin": "50px"}
                        )
                    ]),
            ]
        ),
        html.Div(
            style=css_custom.flex_row,
            children=[
                html.H1(children='Sensor', style={'margin': '5px'}),
                html.H1(children='', id="h1_sensors", style={'margin': '5px'}),
            ]),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                dcc.Graph(id='sensor_battery'),
                dcc.Graph(id='sensor_temperature')
            ]
        ),
        html.Div(
            style=css_custom.flex_row_space_around,
            children=[
                dcc.Graph(id='sensor_fan'),
            ]
        )
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
        Output('h1_disk', 'children'),
        Output('disk_io_counter_bytes_read', 'children'),
        Output('disk_io_counter_bytes_write', 'children'),
        Output('disk_io_counter_read', 'children'),
        Output('disk_io_counter_write', 'children'),
        Output('h1_sensors', 'children'),
        Output('sensor_battery', 'figure'),
        Output('sensor_temperature', 'figure'),
        Output('sensor_fan', 'figure'),
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
    """ Function Callback App
    :param agent: string agent
    :param time: string time
    :return: app
    """
    return agent, \
           get_bar_tab(agent, time), \
           get_indicator('CPU Percent', agent, "cpu", "cpu_percent", time, " %"), \
           get_indicator("CPU Time Percent User", agent, "cpu", "cpu_times_percent_user", time, " %"), \
           get_indicator("CPU Time Percent Idle", agent, "cpu", "cpu_times_percent_idle", time, " %"), \
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
           'Received: ' + str(get_text(agent, "net", "net_io_counters_packets_recv", time)) + " packets", \
           agent, \
           'Read: ' '{:,.0f}'.format(
               get_text(agent, "disk", "disk_io_counters_read_bytes", time) / float(1 << 30)) + " GB", \
           'Write: ' '{:,.0f}'.format(
               get_text(agent, "disk", "disk_io_counters_write_bytes", time) / float(1 << 30)) + " GB", \
           'Read: ' + str(get_text(agent, "disk", "disk_io_counters_read_count", time)), \
           'Write: ' + str(get_text(agent, "disk", "disk_io_counters_write_count", time)), \
           agent, \
           get_indicator('Battery Percent', agent, "sensor", "sensors_battery_percent", time, " %"), \
           get_indicator('Temperature', agent, "sensor", "sensors_temperatures_acpitz_0_current", time, " °C"), \
           get_indicator('Speed Fan', agent, "sensor", "sensors_fans_thinkpad_0_current", time, " RPM"),


if __name__ == '__main__':
    app.run_server(debug=True)
