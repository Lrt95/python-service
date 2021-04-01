""" Module fetch data api

Created by Antony Correia
Python Docstring
"""
import requests


def get_data_agent_hardware(agent=None, hardware=None, time=None, element=None):
    """ Function get data data agent hardware
    :param element:
    :param agent: string agent
    :param hardware: string hardware
    :param time: string time
    :return: data agent hardware
    """
    requests_url = "http://127.0.0.1:5000/?"
    if agent:
        requests_url += "&id=" + agent
    if hardware:
        requests_url += "&hardware=" + hardware
    if time:
        requests_url += "&time=" + time
    if element:
        requests_url += "&element=" + element

    response = requests.get(requests_url)
    return response.json()
