⏱ 0:00 – 0:30 | Intro

“Hi, this is my Python CLI Alarm Clock project.

This is a modular command-line application built using only Python standard library. The goal was to design a clean, maintainable system that supports alarm creation, deletion, listing, and background alarm triggering using threading.

I’ll walk through the architecture, key design decisions, and a quick live demo.”

⏱ 0:30 – 1:30 | Project Structure

“Let me first show the project structure.

The system is split into four modules:

main.py handles the CLI menu and user interaction
manager.py is responsible for alarm storage and operations like add, delete, and list
clock.py handles time display functionality
alarm.py runs the background service that continuously checks and triggers alarms

This separation follows a modular design principle to keep responsibilities isolated and maintainable.”

⏱ 1:30 – 2:30 | Key Design Decisions

“I want to highlight a few key engineering decisions.

First, I used in-memory storage for alarms because there was no requirement for persistence or database integration.

Second, I used threading for the alarm service. The reason I chose threading over asyncio is because this is a simple CLI application, and a background polling thread is sufficient and easier to manage.

The alarm service runs independently and checks every second without blocking the main CLI menu.

Third, I ensured input validation for HH:MM format and also prevented duplicate alarms to avoid redundant triggers.”

⏱ 2:30 – 3:30 | Core Logic Walkthrough

“Now I’ll briefly show the core logic.

In the manager module, alarms are stored in a list and operations like add, delete, and list are handled there.

In the alarm module, there is a background thread that continuously checks the current system time against stored alarms every second.

When a match is found, it triggers a visual alert and a bell sound notification in the terminal.

The main module integrates everything and provides a simple menu-driven interface for the user.”

⏱ 3:30 – 4:30 | Live Demo

“Now I’ll run the application.

Here I start the program, and I can see the CLI menu.

I’ll add an alarm using HH:MM format.

The alarm is stored successfully, and I can list active alarms.

Now I start the alarm service in the background.

When the system time matches the alarm time, you can see the alert triggering without blocking the CLI.

I can still interact with the menu while the background thread is running.”

⏱ 4:30 – 5:00 | Validation + Closing

“I tested the system for multiple cases including invalid time input, duplicate alarm prevention, and concurrent execution while the CLI remains responsive.

Overall, the focus of this implementation was on clean modular design, correct concurrency handling, and maintainable structure rather than adding unnecessary features.

That’s the end of the walkthrough. Thank you.”