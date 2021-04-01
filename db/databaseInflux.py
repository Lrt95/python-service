""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "Tzwjjay6Dv9j6dg1-P-Kq3yulo6t0y4-Ze17fe_VrV8HVijPrzE-B65hcVQF9tFaiVmBvj2xhnQKVC3WNCSuhg=="
org = "antony.correia@gmail.com"
bucket = "antony.correia's Bucket"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


def write_data(hardware_element, hardware, agent):
    """ Function write data disk
        in InFluxDB
    :param agent: string of agent
    :param hardware: string of type hardware
    :param hardware_element: dict hardware element
    """
    for field, value in hardware_element.items():
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point("data") \
            .tag("agent", agent) \
            .tag("hardware", hardware) \
            .field(field, value) \
            .time(datetime.utcnow(), WritePrecision.NS)
        write_api.write(bucket, org, point)


def read_data_agent_hardware(time, agent, hardware):
    """ Function read_data_agent_hardware
        in InFluxDB
    :param time: time for query
    :param agent: string of agent
    :param hardware: string of type hardware
    :return: list of result query
    """
    query = f'from(bucket: \"{bucket}\")\
    |> range(start: -' + str(time) + 'h)\
    |> filter(fn: (r) => r._measurement == "data")\
    |> filter(fn: (r) => r.agent == "agent' + str(agent) + '")\
    |> filter(fn: (r) => r.hardware == "' + str(hardware) + '")'

    result = client.query_api().query(org=org, query=query)
    result_query = []
    result_hardware = {}
    dict_system = {}
    for table in result:

        result_hardware["elements"] = []
        for line in table:
            result_hardware["time"] = line["_time"]
            result_hardware["agent"] = line["agent"]
        for record in table.records:
            dict_system[record.get_field()] = record.get_value()
        result_hardware["elements"].append(dict_system)
        result_query.append( result_hardware)

    return result_query


def read_data_agent(time, agent):
    """ Function read_data_agent
        in InFluxDB
    :param time: time for query
    :param agent: id of agent
    :return: list of result query
    """
    query = f'from(bucket: \"{bucket}\")\
    |> range(start: -' + str(time) + 'h)\
    |> filter(fn: (r) => r._measurement == "data")\
    |> filter(fn: (r) => r.agent == "agent' + str(agent) + '")\
    |> sort(columns:["agent"])'

    result = client.query_api().query(org=org, query=query)
    result_query = []
    dict_system = {}
    for table in result:
        result_hardware = {}
        result_hardware["elements"] = []
        for line in table:
            result_hardware["time"] = line["_time"]
            result_hardware["agent"] = line["agent"]
        for record in table.records:
            dict_system[record.get_field()] = record.get_value()
        result_hardware["elements"].append(dict_system)
        result_query.append(result_hardware)

    return result_query


def read_all_data(time):
    """ Function read_all_data
        in InFluxDB
    :param time: time for query
    :return: list of result query
    """
    query = f'from(bucket: \"{bucket}\")\
    |> range(start: -' + str(time) + 'h)\
    |> filter(fn: (r) => r._measurement == "data")\
    |> sort(columns:["agent"])'
    result = client.query_api().query(org=org, query=query)

    result_query = []
    dict_system = {}
    for table in result:
        result_hardware = {}
        result_hardware["elements"] = []
        for line in table:
            result_hardware["agent"] = line["agent"]
            result_hardware["time"] = line["_time"]
            for record in table.records:
                dict_system[record.get_field()] = record.get_value()
        result_hardware["elements"].append(dict_system)
        result_query.append(result_hardware)

    return result_query


if __name__ == '__main__':
    read_data_agent_hardware(12, 0, "cpu")
