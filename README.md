# Python CLI Alarm Clock

A modular command-line alarm clock application built with Python standard library.

## Design & Architecture

### Overview
The application follows a modular design with 4 separate modules, each responsible for a specific aspect of functionality:

- **main.py** - Entry point, menu loop, and threading orchestration
- **clock.py** - Time display functionality
- **manager.py** - Alarm storage and management (in-memory list)
- **alarm.py** - Background alarm checking service

### Module Responsibilities

#### main.py
- Displays menu with 6 options
- Shows active alarm count on menu
- Handles user input and input validation
- Manages background alarm thread with daemon=True
- Handles KeyboardInterrupt and EOFError gracefully

#### clock.py
- `show_clock()` function displays current time in HH:MM:SS format
- Updates every second using `\r` carriage return
- Returns to menu on Ctrl+C

#### manager.py
- In-memory alarm storage using a list
- `add_alarm(t)` - Validates HH:MM format, prevents duplicates
- `delete_alarm(t)` - Requires user confirmation before deleting
- `list_alarms()` - Displays all alarms sorted numerically
- `get_alarms()` - Returns copy of alarms list
- `validate_time_format(t)` - Uses datetime.strptime to validate HH:MM format

#### alarm.py
- `run_alarm_checker()` - Background service that polls every 10 seconds
- Compares current time against stored alarms
- Triggers alarm with visual banner and terminal bell (`\a`)
- Automatically removes triggered alarms

## Features Implemented

- [x] 6-option menu (Show Clock, Add Alarm, Delete Alarm, List Alarms, Start Alarm Service, Exit)
- [x] Display active alarm count on menu
- [x] Add alarm with HH:MM format validation
- [x] Prevent duplicate alarm entries
- [x] Delete alarm with y/n confirmation prompt
- [x] List all alarms sorted and numbered
- [x] Background alarm service using threading
- [x] Alarm triggers with visual banner and bell sound
- [x] Graceful exit with Ctrl+C or option 6
- [x] Invalid input handled gracefully

## Requirements

- Python 3.x (no external dependencies)
- Uses only standard library modules:
  - `datetime` - Time handling
  - `time` - Sleep and timing
  - `threading` - Background alarm service
  - `sys` - Exit handling

## How to Run

```bash
cd alarm_clock
python main.py
```

Or from parent directory:
```bash
python -m alarm_clock.main
```

## Usage

1. Run `python main.py`
2. Menu displays with active alarm count
3. Choose options:
   - **1** - Show current clock (Ctrl+C to return to menu)
   - **2** - Add alarm (enter time in HH:MM format)
   - **3** - Delete alarm (enter time, confirm with y/n)
   - **4** - List all alarms
   - **5** - Start background alarm service
   - **6** - Exit application

## Example Session

```
========================================
         PYTHON ALARM CLOCK
========================================
   Active Alarms: 0
----------------------------------------
  1. Show Current Clock
  2. Add Alarm
  3. Delete Alarm
  4. List Alarms
  5. Start Alarm Service
  6. Exit
----------------------------------------

Enter your choice (1-6): 2
Enter alarm time (HH:MM): 14:30
[+] Alarm '14:30' added successfully!
```