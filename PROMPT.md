# Prompt

Build a Python CLI Alarm Clock application with the following requirements:

## Requirements

1. **Modular Architecture**: Split into 4 files:
   - `main.py` - Entry point with menu loop
   - `clock.py` - Shows current time in HH:MM:SS format
   - `manager.py` - Manages alarms (add, delete, list)
   - `alarm.py` - Background service that checks and triggers alarms

2. **Menu Options** (6 options):
   - Show Current Clock
   - Add Alarm
   - Delete Alarm
   - List Alarms
   - Start Alarm Service
   - Exit

3. **Features**:
   - Display active alarm count on menu
   - Add alarm with HH:MM format validation
   - Prevent duplicate alarms
   - Delete alarm with confirmation prompt
   - List alarms sorted and numbered
   - Background alarm service using threading
   - Alarm triggers with visual banner and bell sound
   - Handle invalid input gracefully
   - Use only Python standard library (no external dependencies)

4. **Technical Details**:
   - Use threading for background alarm service
   - Poll alarms every 1 seconds
   - Use in-memory storage for alarms
   - Handle KeyboardInterrupt and EOFError

## Design & Architecture

The application follows a modular design where each module has a single responsibility:

- **main.py**: Entry point, menu loop, and threading orchestration
- **clock.py**: Time display functionality
- **manager.py**: Alarm storage and management (in-memory list)
- **alarm.py**: Background alarm checking service

## How to Run

```bash
cd alarm_clock
python main.py
```