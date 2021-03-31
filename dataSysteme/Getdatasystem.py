""" Module GetDataSystem

Created by Emerick CHALET
Python Docstring
"""
from enum import Enum

import psutil
import platform


class GetDataSystem:
    """ Class GetDataSystem"""

    def __init__(self):
        pass

    @staticmethod
    def get_cpu_times():
        """ Method get cpu times
        :rtype: object cpu times
        """
        return psutil.cpu_times(percpu=False)

    @staticmethod
    def get_cpu_percent():
        """ Method get cpu percent
        :rtype: object cpu percent
        """
        return psutil.cpu_percent(interval=None, percpu=False)

    @staticmethod
    def get_cpu_times_percent():
        """ Method get cpu times percent
        :rtype: object cpu times percent
        """
        return psutil.cpu_times_percent(interval=None, percpu=False)

    @staticmethod
    def get_cpu_stats():
        """ Method get cpu stats
        :rtype: object cpu stats
        """
        return psutil.cpu_stats()

    @staticmethod
    def get_cpu_load_avg():
        """ Method get load avg
        :rtype: object load avg
        """
        return psutil.getloadavg()

    @staticmethod
    def get_virtual_memory():
        """ Method get virtual memory
        :rtype: object virtual memory
        """
        return psutil.virtual_memory()

    @staticmethod
    def get_swap_memory():
        """ Method get swap memory
        :rtype: object swap memory
        """
        return psutil.swap_memory()

    @staticmethod
    def get_disk_partitions():
        """ Method get disk partitions
        :rtype: object get disk partitions
        """
        return psutil.disk_partitions(all=False)

    @staticmethod
    def get_disk_usage(path):
        """ Method get disk usage
        :param path: string of path disk
        :return: dict disk usage
        """
        return psutil.disk_usage(path)

    @staticmethod
    def get_disk_io_counters():
        """ Method get disk io counters
        :rtype: object get disk io counters
        """
        return psutil.disk_io_counters()

    @staticmethod
    def get_net_io_counters():
        """ Method get net io counters
        :rtype: object net disk io counters
        """
        return psutil.net_io_counters(pernic=False, nowrap=True)

    @staticmethod
    def get_sensors_temperatures():
        """ Method get sensors temperatures
        :rtype: object get sensors temperatures
        """
        return psutil.sensors_temperatures(fahrenheit=False)

    @staticmethod
    def get_sensors_fans():
        """ Method get sensors fans
        :rtype: object get sensors fans
        """
        return psutil.sensors_fans()

    @staticmethod
    def get_sensors_battery():
        """ Method get sensors battery
        :rtype: object get sensors battery
        """
        return psutil.sensors_battery()

    def create_dictionary_cpu(self):
        """ Method create dictionary cpu
        :return: dict of info cpu
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
        """ Method create dictionary memory
        :return: dict of info memory
        """
        dictionary_memory = {}

        self.set_dict(dictionary_memory, self.get_virtual_memory(), "virtual_memory_")
        self.set_dict(dictionary_memory, self.get_swap_memory(), "swap_memory_")

        return dictionary_memory

    def create_dictionary_disk(self):
        """ Method create dictionary disk
        :return: dict of info disk
        """
        dictionary_disk = {}

        path = "C://" if platform.platform() == "Windows" else "/"
        self.set_dict_disk(dictionary_disk, self.get_disk_partitions(), "disk_partitions_")
        self.set_dict(dictionary_disk, self.get_disk_usage(path), "disk_usage_")
        self.set_dict(dictionary_disk, self.get_disk_io_counters(), "disk_io_counters_")
        return dictionary_disk

    def create_dictionary_net(self):
        """ Method create dictionary net
        :return: dict of info net
        """
        dictionary_net = {}

        self.set_dict(dictionary_net, self.get_net_io_counters(), "net_io_counters_")

        return dictionary_net

    def create_dictionary_sensors(self):
        """ Method create dictionary sensors
        :return: dict of info sensors
        """
        dictionary_sensors = {}
        self.set_dict(dictionary_sensors, self.get_sensors_battery(), "sensors_battery_")
        if platform.platform() == "Linux":
            self.set_dict_sensor(dictionary_sensors, self.get_sensors_temperatures(), "sensors_temperatures_")
            self.set_dict_sensor(dictionary_sensors, self.get_sensors_fans(), "sensors_fans_")

        return dictionary_sensors

    @staticmethod
    def set_dict_sensor(dictionary_sensors, sensors, key_name):
        """ Method set dict sensor
            Iterate of object sensor for create dict of sensors
        :param dictionary_sensors: dict of sensors
        :param sensors: object sensors
        :param key_name: string of key
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
        """ Method set dict
            Iterate of object info system for create dict
        :param dictionary_net: dict
        :param named_tuple: Object namedtuple
        :param key_name: string of key
        """
        index = 0
        for element in named_tuple:
            dictionary_net[key_name + named_tuple._fields[index]] = element.value if isinstance(element,
                                                                                                Enum) else element
            index += 1

    @staticmethod
    def set_dict_disk(dictionary_disk, disk, key_name):
        """ Method set dict disk
            Iterate of object disk for create dict of disk
        :param dictionary_disk: dict of disk
        :param disk: object disk
        :param key_name: string of key name
        """
        index_ = 0
        for value in disk:
            index = 0
            for element in value:
                dictionary_disk[
                    key_name + str(index_) + "_" + str(index) + "_" + value._fields[index]] = element
                index += 1
            index_ += 1
