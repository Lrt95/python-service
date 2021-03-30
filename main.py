""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler

interval_schedule = 3


def lauch_task():
    """Function launch task
        For lunch task to schedule
    """
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(lauch_task, 'interval', seconds=interval_schedule)
    scheduler.start()
    print('Press Ctrl + C to exit')

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
