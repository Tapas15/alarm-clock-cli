"""Alarm management module - handles adding, deleting, and listing alarms."""

import datetime

alarms = []


def add_alarm(t):
    """
    Add an alarm at the specified time.
    
    Args:
        t (str): Time in HH:MM format
    
    Returns:
        bool: True if alarm was added, False otherwise
    """
    if not validate_time_format(t):
        print(f"[!] Invalid time format: '{t}'. Please use HH:MM format.")
        return False
    
    if t in alarms:
        print(f"[!] Alarm '{t}' already exists!")
        return False
    
    alarms.append(t)
    print(f"[+] Alarm '{t}' added successfully!")
    return True


def delete_alarm(t):
    """
    Delete an alarm at the specified time.
    
    Args:
        t (str): Time in HH:MM format
    
    Returns:
        bool: True if alarm was deleted, False otherwise
    """
    if t in alarms:
        confirm = input(f"Are you sure you want to delete alarm '{t}'? (y/n): ").strip().lower()
        if confirm == 'y':
            alarms.remove(t)
            print(f"[+] Alarm '{t}' deleted successfully!")
            return True
        else:
            print("[!] Deletion cancelled.")
            return False
    else:
        print(f"[!] Alarm '{t}' not found!")
        return False


def remove_alarm(t):
    """
    Remove an alarm without confirmation (used by alarm checker).
    
    Args:
        t (str): Time in HH:MM format
    """
    if t in alarms:
        alarms.remove(t)


def list_alarms():
    """
    List all currently set alarms.
    """
    if not alarms:
        print("[*] No alarms set.")
    else:
        print(f"\n[*] Active Alarms ({len(alarms)}):")
        print("-" * 20)
        for i, alarm in enumerate(sorted(alarms), 1):
            print(f"   {i}. {alarm}")
        print("-" * 20)


def get_alarms():
    """
    Get a copy of the alarms list.
    
    Returns:
        list: Copy of the alarms list
    """
    return alarms.copy()


def validate_time_format(t):
    """
    Validate that time is in HH:MM format.
    
    Args:
        t (str): Time string to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        datetime.datetime.strptime(t, "%H:%M")
        return True
    except ValueError:
        return False