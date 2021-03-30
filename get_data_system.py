""" Module Main

Created by Emerick CHALET
Python Docstring
"""
import psutil


class get_data_system():
    def __init__(self):
        pass

    def get_cpu_percent(self):
        """

        :rtype: object
        """
        cpu_percent = psutil.cpu_percent(interval=1)
        return cpu_percent

    def get_cpu_count(self):
        """

        :rtype: object
        """
        cpu_count = psutil.cpu_count()
        return cpu_count

    def get_cpu_stats(self):
        """

        :rtype: object
        """
        cpu_stats = psutil.cpu_stats()
        return cpu_stats

    def get_cpu_freq(self):
        """

        :rtype: object
        """
        cpu_freq = psutil.cpu_freq()
        return cpu_freq

    def get_virtual_memory(self):
        """

        :rtype: object
        """
        virtual_memory = psutil.virtual_memory()
        return virtual_memory

    def get_swap_memory(self):
        """

        :rtype: object
        """
        swap_memory = psutil.swap_memory()
        return swap_memory

    def get_disk_partitions(self):
        """

        :rtype: object
        """
        disk_partitions = psutil.disk_partitions()
        return disk_partitions

    def get_disk_io_counters(self):
        """

        :rtype: object
        """
        disk_io_counters = psutil.disk_io_counters()
        return disk_io_counters

    def get_net_io_counters(self):
        """

        :rtype: object
        """
        net_io_counters = psutil.net_io_counters()
        return net_io_counters

    def get_sensors_battery(self):
        """

        :rtype: object
        """
        sensors_temperature = psutil.sensors_battery()
        return sensors_temperature

    def create_dictionary_cpu(self):
        """

        :rtype: object
        """
        dictionary_cpu = {"cpu_percent": self.get_cpu_percent(), "cpu_count": self.get_cpu_count(),
                          "cpu_stats": self.get_cpu_stats(),
                          "cpu_freq": self.get_cpu_freq()}
        return dictionary_cpu

    def create_dictionary_memory(self):
        """

        :rtype: object
        """
        dictionary_memory = {"virtual_memory": self.get_virtual_memory(), "swap_memory": self.get_swap_memory()}
        return dictionary_memory

    def create_dictionary_disk(self):
        """

        :rtype: object
        """
        dictionary_disk = {"disk_partitions": self.get_disk_partitions(),
                           "disk_io_counters": self.get_disk_io_counters()}
        return dictionary_disk

    def create_dictionary_net(self):
        """

        :rtype: object
        """
        dictionary_net = {"net_io_counters": self.get_net_io_counters()}
        return dictionary_net

    def create_dictionary_sensors(self):
        """

        :rtype: object
        """
        dictionary_sensors = {"sensors_battery": self.get_sensors_battery()}
        return dictionary_sensors
