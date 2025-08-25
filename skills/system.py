import os

def execute(command: str) -> str:
    command = command.lower()
    if "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the system."
    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting the system."
    elif "sleep" in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "Putting the system to sleep."
    else:
        return "System command not recognized."
