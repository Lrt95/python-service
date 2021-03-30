""" Module Main

Created by Emerick CHALET
Python Docstring
"""
import psutil
from collections import namedtuple


class GetDataSystem():
    def __init__(self):
        pass

    def get_cpu_times(self):
        """

        :rtype: object
        """
        return psutil.cpu_times(percpu=False)

    def get_cpu_percent(self):
        """

        :rtype: object
        """
        return psutil.cpu_percent(interval=None, percpu=False)

    def get_cpu_times_percent(self):
        """

        :rtype: object
        """
        return psutil.cpu_times_percent(interval=None, percpu=False)


    def get_cpu_stats(self):
        """

        :rtype: object
        """
        return psutil.cpu_stats()

    def get_cpu_load_avg(self):
        """

        :rtype: object
        """
        return psutil.getloadavg()


    def get_virtual_memory(self):
        """

        :rtype: object
        """
        return psutil.virtual_memory()

    def get_swap_memory(self):
        """

        :rtype: object
        """
        return psutil.swap_memory()

    def get_disk_partitions(self):
        """

        :rtype: object
        """
        return psutil.disk_partitions(all=False)

    def get_disk_usage(self, path):
        """

        :rtype: object
        """
        return psutil.disk_usage(path)

    def get_disk_io_counters(self):
        """

        :rtype: object
        """
        return psutil.disk_io_counters()

    def get_net_io_counters(self):
        """

        :rtype: object
        """
        return psutil.net_io_counters(pernic=False, nowrap=True)

    def get_sensors_temperatures(self):
        """

        :rtype: object
        """
        return psutil.sensors_temperatures(fahrenheit=False)

    def get_sensors_fans(self):
        """

        :rtype: object
        """
        return psutil.sensors_fans()

    def get_sensors_battery(self):
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

        index_times = 0
        for value in self.get_cpu_times():
            dictionary_cpu["cpu_times_" + self.get_cpu_times()._fields[index_times]] = value
            index_times += 1

        index_times_percent = 0
        for value in self.get_cpu_times_percent():
            dictionary_cpu["cpu_times_percent_" + self.get_cpu_times_percent()._fields[index_times_percent]] = value
            index_times_percent += 1

        index_cpu_stats = 0
        for value in self.get_cpu_stats():
            dictionary_cpu["cpu_stats_" + self.get_cpu_stats()._fields[index_cpu_stats]] = value
            index_cpu_stats += 1
        return dictionary_cpu

    def create_dictionary_memory(self):
        """

        :rtype: object
        """
        dictionary_memory = {}

        index_virtual_memory = 0
        for value in self.get_virtual_memory():
            dictionary_memory["virtual_memory_" + self.get_virtual_memory()._fields[index_virtual_memory]] = value
            index_virtual_memory += 1

        index_swap_memory = 0
        for value in self.get_swap_memory():
            dictionary_memory["swap_memory_" + self.get_swap_memory()._fields[index_swap_memory]] = value
            index_swap_memory += 1

        return dictionary_memory

    def create_dictionary_disk(self):
        """

        :rtype: object
        """
        dictionary_disk = {
            "disk_partitions": self.get_disk_partitions(),
            # "disk_usage": self.get_disk_usage(),
            "disk_io_counters": self.get_disk_io_counters()
        }
        return dictionary_disk

    def create_dictionary_net(self):
        """

        :rtype: object
        """
        dictionary_net = {
            "net_io_counters": self.get_net_io_counters()
        }
        return dictionary_net

    def create_dictionary_sensors(self):
        """

        :rtype: object
        """
        dictionary_sensors = {
            "sensors_temperatures": self.get_sensors_temperatures(),
            "sensors_fans": self.get_sensors_fans(),
            "sensors_battery": self.get_sensors_battery()
        }
        return dictionary_sensors
