""" Module Figure Custom

Created by Antony Correia
Python Docstring
"""
from dashboard.request_api.fetch_data_api import get_data_agent_hardware
from dateutil.parser import parse
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

colors = px.colors.qualitative.Plotly

def get_cpu_load_avg(data_api, agent):
    """ Function get cpu load avg
    :param agent: string agent name
    :param data_api: list data cpu
    :return:
    """
    return {
        "cpu_load_avg_1minutes": data_api[agent]["cpu_load_avg_1minutes"][-1]["value"] * 10 \
            if data_api else 0,
        "cpu_load_avg_5minutes": data_api[agent]["cpu_load_avg_5minutes"][-1]["value"] * 10 \
            if data_api else 0,
        "cpu_load_avg_15minutes": data_api[agent]["cpu_load_avg_15minutes"][-1]["value"] * 10 \
            if data_api else 0
    }


def get_indicator(title, agent, hardware, element, time, suffix):
    """ Function get indicator
     :param suffix: string suffix
     :param time: string time
     :param hardware: string hardware
     :param element: string element
     :param agent: string agent
     :param title: string title
    :return:
    """
    range_indicator = []
    range_good = []
    range_bad = []
    if suffix == " %":
        range_indicator = [0, 100]
        range_good = [0, 80]
        range_bad = [80, 100]
    elif suffix == " °C":
        range_indicator = [0, 100]
        range_good = [0, 80]
        range_bad = [80, 100]
    elif suffix == " RPM":
        range_indicator = [0, 10000]
        range_good = [0, 8000]
        range_bad = [8000, 10000]

    data = get_data_agent_hardware(agent=agent, hardware=hardware, element=element, time=time)
    indicator = go.Figure(go.Indicator(
        mode="gauge+number",
        number={'suffix': suffix, 'font': {'size': 50}},
        value=data[agent][element][-1]["value"] if data else 0,
        title={'text': title},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': range_indicator},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': range_good, 'color': 'green'},
                {'range': range_bad, 'color': 'red'}]
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
    if range_yaxis is None:
        range_yaxis = []
    if agent is None:
        agent = ""
    data = get_data_agent_hardware(agent=agent, hardware="cpu", time=time, element=element)
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
    for agent, elements in data.items():
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
    """ Function get pie
    :param agent: string agent
    :param elements: list elements
    :param total: string element total
    :param time: string time
    :return: figure pie chart
    """
    labels = []
    values = []
    title = 0.0
    for element in elements:
        data = get_data_agent_hardware(agent=agent, hardware="memory", time=time, element=element)
        if not data:
            break
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
    data = get_data_agent_hardware(agent=agent, hardware="cpu", time=time)
    cpu_load_avg = get_cpu_load_avg(data, agent)
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
    """ Function get text
    :param agent: string agent
    :param hardware: string hardware
    :param element: string element
    :param time: string time
    :return: text
    """
    data = get_data_agent_hardware(agent=agent, hardware=hardware, element=element, time=time)
    if not data:
        return 0.0
    return data[agent][element][-1]['value']