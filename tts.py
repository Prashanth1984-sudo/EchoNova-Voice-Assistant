import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Try male=0 / female=1 depending on system
engine.setProperty("rate", 175)
engine.setProperty("volume", 1)

def speak(text: str):
    print(f"Jarvis: {text}")  # Debug print
    engine.say(text)
    engine.runAndWait()
