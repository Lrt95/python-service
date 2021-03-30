""" Module Main

Created by Emerick CHALET
Python Docstring
"""
import psutil


def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent


def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count


def get_cpu_stats():
    cpu_stats = psutil.cpu_stats()
    return cpu_stats


def get_cpu_freq():
    cpu_freq = psutil.cpu_freq()
    return cpu_freq


def get_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    return virtual_memory


def get_swap_memory():
    swap_memory = psutil.swap_memory()
    return swap_memory


def get_disk_partitions():
    disk_partitions = psutil.disk_partitions()
    return disk_partitions


def get_disk_io_counters():
    disk_io_counters = psutil.disk_io_counters()
    return disk_io_counters



def main():
    print(get_cpu_percent())
    print(get_cpu_count())
    print(get_cpu_stats())
    print(get_cpu_freq())
    print(get_virtual_memory())
    print(get_swap_memory())
    print(get_disk_partitions())
    print(get_disk_io_counters())

if __name__ == '__main__':
    main()
