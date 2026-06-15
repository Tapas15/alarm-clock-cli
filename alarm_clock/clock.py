"""Clock display module - shows current time in HH:MM:SS format."""

import datetime
import time


def show_clock():
    """
    Display the current time in HH:MM:SS format.
    Updates every second continuously until interrupted by user (Ctrl+C).
    """
    print("\n[*] Current Clock - Press Ctrl+C to return to menu")
    print("-" * 30)
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\r{current_time}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" + "-" * 30)
        print("Returning to menu...")