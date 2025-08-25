import datetime

def execute(command: str) -> str:
    command = command.lower()

    if "time" in command:
        return f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "date" in command:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"
    else:
        return "Info command not recognized."
