import sounddevice as sd
import numpy as np
import queue
import speech_recognition as sr

class Recognizer:
    def __init__(self, device_index=None, samplerate=44100):
        self.device_index = device_index
        self.samplerate = samplerate
        self.recognizer = sr.Recognizer()
        self.audio_queue = queue.Queue()

    def _callback(self, indata, frames, time, status):
        """Internal callback for sounddevice."""
        if status:
            print(f"Audio status: {status}")
        self.audio_queue.put(indata.copy())

    def listen(self, duration=5):
        """Listen from the microphone and return recognized text."""
        try:
            print(f"Listening on device {self.device_index}, samplerate {self.samplerate}...")
            with sd.InputStream(samplerate=self.samplerate,
                                channels=1,
                                device=self.device_index,
                                callback=self._callback):
                frames = []
                for _ in range(int(self.samplerate / 1024 * duration)):
                    data = self.audio_queue.get()
                    frames.append(data)

                audio_data = np.concatenate(frames, axis=0)
                audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()

                audio = sr.AudioData(audio_bytes, self.samplerate, 2)

                try:
                    text = self.recognizer.recognize_google(audio)
                    print(f"Detected text: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Jarvis: I didn't catch that.")
                    return ""
                except sr.RequestError as e:
                    print(f"Speech Recognition API error: {e}")
                    return ""
        except Exception as e:
            print(f"Microphone error: {e}")
            return ""
