import os
import subprocess
import webbrowser
from utils import battery_status, os_name

APP_MAP = {
    "notepad": r"notepad.exe",
    "calculator": r"calc.exe",
    "vscode": r"code",
    "chrome": r"chrome",
}

def open_app(app: str) -> str:
    key = app.lower().strip()
    cmd = APP_MAP.get(key)
    if not cmd:
        return f"I don't know how to open {app} yet."
    try:
        subprocess.Popen(cmd, shell=True)
        return f"Opening {app}."
    except Exception:
        return f"Failed to open {app}."

def open_site(name: str, sites: dict) -> str:
    url = sites.get(name.lower())
    if not url:
        return f"I don't have a site for {name}."
    webbrowser.open(url)
    return f"Opening {name}."

def search_web(query: str) -> str:
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching the web for {query}."

def system_info(intent: str) -> str:
    if "battery" in intent:
        return "Battery is " + battery_status()
    return ""
