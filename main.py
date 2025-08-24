import pyttsx3
from recognizer import Recognizer  # your updated Recognizer class

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    rec = Recognizer()  # Initialize your recognizer
    speak("Hello sir, what's going on?")
    print("Jarvis: Hello sir, what's going on?")

    retries = 3  # number of attempts to listen per command

    while True:
        command = ""
        for attempt in range(retries):
            print("Listening...")
            command = rec.listen(duration=5)
            if command.strip():
                break
            else:
                print(f"Jarvis: I heard nothing, please repeat. ({retries - attempt - 1} attempts left)")
                speak("I heard nothing, please repeat.")

        if not command.strip():
            print("Jarvis could not hear anything after multiple attempts.")
            speak("I could not hear anything.")
            continue

        print(f"Recognized command: {command}")
        speak(f"You said: {command}")

        # Example exit command
        if "exit" in command.lower() or "quit" in command.lower():
            speak("Goodbye sir!")
            print("Jarvis: Goodbye sir!")
            break

if __name__ == "__main__":
    main()
