import os
import webbrowser
import datetime
from tts import speak

def handle_command(command: str):
    command = command.lower()

    if "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc.exe")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open browser" in command:
        speak("Opening your default browser")
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")

    elif "take rest" in command or "shutdown" in command:
        speak("Okay sir, shutting down. Have a nice day!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")
