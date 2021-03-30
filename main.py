""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler

from db.databaseInflux import DatabaseInflux

interval_schedule = 3


def launch_task():
    """Function launch task
        For lunch task to schedule
    """
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(launch_task, 'interval', seconds=interval_schedule)
    scheduler.start()
    print('Press Ctrl + C to exit')
    db = DatabaseInflux("agent1")
    db.write_data({"disk_partitions": 234.25, "disk_io_counters": 254}, "disk")
    print(db.read_data("disk"))
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
