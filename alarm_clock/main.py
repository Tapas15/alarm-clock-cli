"""Main entry point for the Alarm Clock CLI application."""

import threading
import sys
from clock import show_clock
from manager import add_alarm, delete_alarm, list_alarms, get_alarms


alarm_thread = None


def display_menu():
    """Display the main menu options."""
    active_count = len(get_alarms())
    print("\n" + "=" * 40)
    print("         PYTHON ALARM CLOCK")
    print("=" * 40)
    print(f"   Active Alarms: {active_count}")
    print("-" * 40)
    print("  1. Show Current Clock")
    print("  2. Add Alarm")
    print("  3. Delete Alarm")
    print("  4. List Alarms")
    print("  5. Start Alarm Service")
    print("  6. Exit")
    print("-" * 40)


def main():
    """Main function containing the menu loop."""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                show_clock()
            
            elif choice == "2":
                time_input = input("Enter alarm time (HH:MM): ").strip()
                add_alarm(time_input)
            
            elif choice == "3":
                time_input = input("Enter alarm time to delete (HH:MM): ").strip()
                delete_alarm(time_input)
            
            elif choice == "4":
                list_alarms()
            
            elif choice == "5":
                global alarm_thread
                if alarm_thread and alarm_thread.is_alive():
                    print("[*] Alarm service is already running!")
                else:
                    from alarm import run_alarm_checker
                    alarm_thread = threading.Thread(target=run_alarm_checker, daemon=True)
                    alarm_thread.start()
                    print("[*] Alarm service started in background!")
            
            elif choice == "6":
                print("\n[+] Goodbye!")
                sys.exit(0)
            
            else:
                print("[!] Invalid choice! Please enter a number between 1-6.")
        
        except EOFError:
            print("\n[+] Goodbye!")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\n\n[+] Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()