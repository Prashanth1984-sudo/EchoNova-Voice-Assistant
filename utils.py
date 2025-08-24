import re
import datetime
import platform
import psutil

SAFE_MATH = re.compile(r"^[0-9\.\+\-\*\/\(\)\s%]+$")

def now_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def today_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def safe_eval_math(expr: str):
    if not SAFE_MATH.match(expr):
        raise ValueError("Unsafe expression")
    return eval(expr, {"__builtins__": {}}, {})

def battery_status():
    try:
        batt = psutil.sensors_battery()
        if not batt: return "Battery information not available."
        plugged = "plugged in" if batt.power_plugged else "on battery"
        return f"{batt.percent:.0f}% and {plugged}."
    except Exception:
        return "Battery information not available."

def os_name():
    return platform.system().lower()
