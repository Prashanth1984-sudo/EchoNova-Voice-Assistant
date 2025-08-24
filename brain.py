import re
from utils import now_time, today_date
from skills.system import open_app, system_info
from skills.web import handle_web
from skills.info import wiki_summary
from skills.mathskill import handle_math

class Brain:
    def __init__(self, config: dict, say_cb):
        self.cfg = config
        self.say = say_cb
        self.wake = config.get("wake_word", "jarvis").lower()

    def is_wake(self, text: str) -> bool:
        return self.wake in text.lower().split()

    def handle(self, text: str) -> str:
        t = text.lower().strip()

        # small talk / control
        if t in ("quit", "exit", "stop", "shutdown"):
            self.say("Goodbye.")
            raise SystemExit
        if any(g in t for g in ["hello", "hi", "hey"]):
            return "Hello! How can I help?"
        if "thank" in t:
            return "Anytime."

        # time & date
        if "time" in t:
            return f"It's {now_time()}."
        if "date" in t or "day" in t:
            return f"Today is {today_date()}."

        # system info
        if "battery" in t:
            return system_info("battery")

        # open app
        m = re.match(r"^open\s+([a-z0-9\.\- ]+)$", t)
        if m:
            return open_app(m.group(1))

        # web / sites / search
        web_ans = handle_web(t, self.cfg.get("open_sites", {}))
        if web_ans:
            return web_ans

        # math
        math_ans = handle_math(t)
        if math_ans:
            return math_ans

        # wikipedia if prefixed
        if t.startswith(("who is", "what is", "tell me about")):
            q = re.sub(r"^(who is|what is|tell me about)\s+", "", t).strip()
            if q:
                return wiki_summary(q)

        # fallback: try Wikipedia quick
        if len(t.split()) <= 8:
            maybe = wiki_summary(t, sentences=1)
            if "couldn't find" not in maybe.lower() and "unavailable" not in maybe.lower():
                return maybe

        return "I didn't catch that. Try 'open notepad', 'search for data science', 'what is neural network', or 'calculate 12*(5+3)'."
