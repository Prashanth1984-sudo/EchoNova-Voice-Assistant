import pyttsx3

class Speaker:
    def __init__(self, voice=None, rate=170, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        # Set voice if specified
        if voice and voice != "auto":
            voices = self.engine.getProperty("voices")
            for v in voices:
                if voice.lower() in v.name.lower():
                    self.engine.setProperty("voice", v.id)
                    break

    def say(self, text: str):
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
