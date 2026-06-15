"""Alarm checking module - runs background service to check and trigger alarms."""

import time
import datetime
from manager import get_alarms, remove_alarm


def run_alarm_checker():
    """
    Run as a background service to check alarms periodically.
    Polls alarms every 10 seconds and triggers them when matched.
    """
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        alarms = get_alarms()
        
        for alarm_time in alarms[:]:  # Iterate over a copy to allow removal
            if alarm_time == current_time:
                print("\n" + "=" * 40)
                print(f"ALARM! Time Reached: {alarm_time}")
                print("=" * 40)
                print('\a')  # Ring terminal bell
                time.sleep(1)  # Prevent multiple triggers in same minute
                remove_alarm(alarm_time)
        
        time.sleep(1)  # Poll every 10 seconds