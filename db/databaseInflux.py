""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


# You can generate a Token from the "Tokens Tab" in the UI
token = "Tzwjjay6Dv9j6dg1-P-Kq3yulo6t0y4-Ze17fe_VrV8HVijPrzE-B65hcVQF9tFaiVmBvj2xhnQKVC3WNCSuhg=="
org = "antony.correia@gmail.com"
bucket = "antony.correia's Bucket"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)


class DatabaseInflux:
    """ Class DatabaseInflux
        to write and read data in DB
    """
    def __init__(self, agent):
        self.agent = agent

    def write_data(self, hardware_element, hardware):
        """ Function write data disk
            in InFluxDB
        :param hardware: string of type hardware
        :param hardware_element: dict hardware element
        """
        for field, value in hardware_element.items():
            write_api = client.write_api(write_options=SYNCHRONOUS)
            point = Point("data") \
                .tag("agent", self.agent) \
                .tag("hardware", hardware) \
                .field(field, value) \
                .time(datetime.utcnow(), WritePrecision.NS)
            write_api.write(bucket, org, point)

    def read_data(self, hardware):
        """ Function read data
            in InFluxDB
        :param hardware: string of type hardware
        :return: list of result query
        """
        query = f'from(bucket: \"{bucket}\")\
        |> range(start: -1h)\
        |> filter(fn: (r) => r._measurement == "data")\
        |> filter(fn: (r) => r.agent == \"{self.agent}\")\
        |> filter(fn: (r) => r.hardware == \"{hardware}\")'

        result = client.query_api().query(org=org, query=query)
        results_query = []
        for table in result:
            for record in table.records:
                results_query.append((record.get_value(), record.get_field()))
        return results_query
