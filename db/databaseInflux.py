""" Module databaseInflux

Created by Antony Correia
Python Docstring
"""

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "Tzwjjay6Dv9j6dg1-P-Kq3yulo6t0y4-Ze17fe_VrV8HVijPrzE-B65hcVQF9tFaiVmBvj2xhnQKVC3WNCSuhg=="
org = "antony.correia@gmail.com"
bucket = "python-service"

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


def read_data(time, agent, hardware, element):
    """ Function read_data
        in InFluxDB
    :param element: string of element
    :param time: time for query
    :param agent: string of agent
    :param hardware: string of type hardware
    :return: list of result query
    """
    query = f'from(bucket: \"{bucket}\")\
    |> range(start: -' + str(time) + ')\
    |> filter(fn: (r) => r._measurement == "data")'

    if agent:
        query += f'|> filter(fn: (r) => r.agent == "' + str(agent) + '")'

    if hardware:
        query += f'|> filter(fn: (r) => r.hardware == "' + str(hardware) + '")'

    if element:
        query += f'|> filter(fn: (r) => r["_field"] == "' + str(element) + '")'

    query += '|> sort(columns:["_time"])'

    result = client.query_api().query(org=org, query=query)
    return get_result_query(result)


def get_result_query(result):
    """ Function result query
    :param result: query
    :return: list result db
    """
    result_query = {}
    for table in result:
        for line in table:
            if not line["agent"] in result_query:
                result_query[line["agent"]] = {}

            if not line["_field"] in result_query[line["agent"]]:
                result_query[line["agent"]][line["_field"]] = []
            result_query[line["agent"]][line["_field"]].append({"time": line["_time"], "value": line["_value"]})

    return result_query

