from dotenv import load_dotenv
import os
load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

from app.history import HistoryManager
from app.commands import load_commands
from app.logger import log_info, log_error
from app.plugin_loader import load_plugins 

plugins = load_plugins()

def main():
    print("🧮 Welcome to the Advanced Python Calculator!")
    print("Type 'menu' to see available commands or 'quit' to exit.")

    history = HistoryManager()
    commands = load_commands()
    commands.update(load_plugins())

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "quit":
            log_info("User exited the calculator.")
            break

        elif user_input.lower() == "menu":
            print("Available commands:", ", ".join(commands.keys()))
            print("Special commands: menu, quit, show, clear, save, load")
            continue

        elif user_input.lower() == "show":
            if history.empty():
                print("No history available.")
            else:
                history.show()
            log_info("Displayed history.")
            continue

        elif user_input.lower() == "clear":
            history.clear()
            print("History cleared.")
            log_info("History cleared.")
            continue

        elif user_input.lower() == "save":
            history.save("history.csv")
            print("History saved to history.csv.")
            log_info("History saved to history.csv")
            continue

        elif user_input.lower() == "load":
            history.load("history.csv")
            print("History loaded from history.csv.")
            log_info("History loaded from history.csv")
            continue

            # Plugin operation logic
            tokens = user_input.split()
            if len(tokens) == 3:
                try:
                    num1 = float(tokens[0])
                    num2 = float(tokens[1])
                    operation = tokens[2].lower()

                    if operation in plugins:
                        result = plugins[operation](num1, num2)
                        print(f"Result: {result}")
                        history.add(num1, num2, operation, result)
                        log_info(f"Plugin Calculation: {num1} {operation} {num2} = {result}")
                    else:
                        print("Unknown operation. Type 'menu' for available commands.")
                        log_error(f"Unknown plugin operation: {operation}")
                except ValueError:
                    print("Value error: Usage: <num1> <num2> <operation>")
                    log_error("ValueError: Invalid numeric input.")

                    continue

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Usage: <num1> <num2> <operation>")

            num1, num2, operation = parts
            num1 = float(num1)
            num2 = float(num2)

            if operation not in commands:
                raise ValueError(f"Unknown operation '{operation}'")

            command = commands[operation]
            if callable(command): 
                result = command(num1, num2) 
            else: 
                result = command.execute(num1, num2)
            print("Result:", result)
            history.add(num1, num2, operation, result)

            log_info(f"Calculation: {num1} {operation} {num2} = {result}")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            log_error("Attempted division by zero.")
        except ValueError as ve:
            print("Value error:", ve)
            log_error(f"ValueError: {ve}")
        except Exception as e:
            print("Unexpected error:", e)
            log_error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
