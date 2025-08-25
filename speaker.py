import pyttsx3

class Speaker:
    def __init__(self, voice="auto", rate_wpm=170, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate_wpm)
        self.engine.setProperty("volume", float(volume))
        if voice != "auto":
            # try pick a voice containing this substring
            for v in self.engine.getProperty("voices"):
                if voice.lower() in v.name.lower():
                    self.engine.setProperty("voice", v.id)
                    break

    def say(self, text: str, also_print=True):
        if also_print:
            print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
