from recognizer import Recognizer
from brain import handle_command
from tts import speak

def main():
    rec = Recognizer()
    speak("Jarvis online. Awaiting your command.")

    while True:
        text = rec.listen(duration=5)
        if not text.strip():
            continue
        print(f"You said: {text}")
        response = handle_command(text)
        speak(response)

if __name__ == "__main__":
    main()
