""" Module Main

Created by Emerick CHALET
Python Docstring
"""
from enum import Enum

import psutil


class GetDataSystem:
    """ Class GetDataSystem"""

    def __init__(self):
        pass

    @staticmethod
    def get_cpu_times():
        """

        :rtype: object
        """
        return psutil.cpu_times(percpu=False)

    @staticmethod
    def get_cpu_percent():
        """

        :rtype: object
        """
        return psutil.cpu_percent(interval=None, percpu=False)

    @staticmethod
    def get_cpu_times_percent():
        """

        :rtype: object
        """
        return psutil.cpu_times_percent(interval=None, percpu=False)

    @staticmethod
    def get_cpu_stats():
        """

        :rtype: object
        """
        return psutil.cpu_stats()

    @staticmethod
    def get_cpu_load_avg():
        """

        :rtype: object
        """
        return psutil.getloadavg()

    @staticmethod
    def get_virtual_memory():
        """

        :rtype: object
        """
        return psutil.virtual_memory()

    @staticmethod
    def get_swap_memory():
        """

        :rtype: object
        """
        return psutil.swap_memory()

    @staticmethod
    def get_disk_partitions():
        """

        :rtype: object
        """
        return psutil.disk_partitions(all=False)

    @staticmethod
    def get_disk_usage(path):
        """

        :rtype: object
        """
        return psutil.disk_usage(path)

    @staticmethod
    def get_disk_io_counters():
        """

        :rtype: object
        """
        return psutil.disk_io_counters()

    @staticmethod
    def get_net_io_counters():
        """

        :rtype: object
        """
        return psutil.net_io_counters(pernic=False, nowrap=True)

    @staticmethod
    def get_sensors_temperatures():
        """

        :rtype: object
        """
        return psutil.sensors_temperatures(fahrenheit=False)

    @staticmethod
    def get_sensors_fans():
        """

        :rtype: object
        """
        return psutil.sensors_fans()

    @staticmethod
    def get_sensors_battery():
        """

        :rtype: object
        """
        return psutil.sensors_battery()

    def create_dictionary_cpu(self):
        """

        :rtype: object
        """
        dictionary_cpu = {
            "cpu_percent": self.get_cpu_percent(),
            "cpu_load_avg_1minutes": self.get_cpu_load_avg()[0],
            "cpu_load_avg_5minutes": self.get_cpu_load_avg()[1],
            "cpu_load_avg_15minutes": self.get_cpu_load_avg()[2]
        }

        self.set_dict(dictionary_cpu, self.get_cpu_times(), "cpu_times_")
        self.set_dict(dictionary_cpu, self.get_cpu_times_percent(), "cpu_times_percent_")
        self.set_dict(dictionary_cpu, self.get_cpu_stats(), "cpu_stats_")

        return dictionary_cpu

    def create_dictionary_memory(self):
        """

        :rtype: object
        """
        dictionary_memory = {}

        self.set_dict(dictionary_memory, self.get_virtual_memory(), "virtual_memory_")
        self.set_dict(dictionary_memory, self.get_swap_memory(), "swap_memory_")

        return dictionary_memory

    def create_dictionary_disk(self):
        """

        :rtype: object
        """
        dictionary_disk = {}

        self.set_dict_disk(dictionary_disk, self.get_disk_partitions(), "disk_partitions_")
        self.set_dict(dictionary_disk, self.get_disk_usage("/"), "disk_usage_")
        self.set_dict(dictionary_disk, self.get_disk_io_counters(), "disk_io_counters_")

        return dictionary_disk

    def create_dictionary_net(self):
        """

        :rtype: object
        """
        dictionary_net = {}

        self.set_dict(dictionary_net, self.get_net_io_counters(), "net_io_counters_")

        return dictionary_net

    def create_dictionary_sensors(self):
        """

        :rtype: object
        """
        dictionary_sensors = {}

        self.set_dict(dictionary_sensors, self.get_sensors_battery(), "sensors_battery_")
        self.set_dict_sensor(dictionary_sensors, self.get_sensors_temperatures(), "sensors_temperatures_")
        self.set_dict_sensor(dictionary_sensors, self.get_sensors_fans(), "sensors_fans_")

        return dictionary_sensors

    @staticmethod
    def set_dict_sensor(dictionary_sensors, sensors, key_name):
        """

        :param dictionary_sensors:
        :param sensors:
        :param key_name:
        """
        for key, value in sensors.items():
            index = 0
            for element in value:
                index_element = 0
                for i in element:
                    dictionary_sensors[key_name
                                       + key
                                       + "_"
                                       + str(index)
                                       + "_"
                                       + element._fields[index_element]] = i
                    index_element += 1
                index += 1

    @staticmethod
    def set_dict(dictionary_net, named_tuple, key_name):
        """

        :param dictionary_net:
        :param named_tuple:
        :param key_name:
        """
        index = 0
        for element in named_tuple:
            dictionary_net[key_name + named_tuple._fields[index]] = element.value if isinstance(element,
                                                                                                Enum) else element
            index += 1

    @staticmethod
    def set_dict_disk(dictionary_disk, named_tuple, key_name):
        """

        :param dictionary_disk:
        :param named_tuple:
        :param key_name:
        """
        index_ = 0
        for value in named_tuple:
            index = 0
            for element in value:
                dictionary_disk[
                    key_name + str(index_) + "_" + str(index) + "_" + value._fields[index]] = element
                index += 1
            index_ += 1