from datetime import datetime

def now_time():
    return datetime.now().strftime("%I:%M %p")

def today_date():
    return datetime.now().strftime("%B %d, %Y")
