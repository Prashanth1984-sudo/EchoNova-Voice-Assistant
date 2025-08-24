import sounddevice as sd
import numpy as np
import json
from vosk import Model, KaldiRecognizer
from scipy.signal import resample

class Recognizer:
    def __init__(self, model_path="models/vosk-model-small-en-us-0.15"):
        self.model = Model(model_path)
        self.recognizer = None
        self.channels = 1  # default mono

        # Select microphone automatically
        self.device_index, self.samplerate, self.channels = self.get_input_device()

        # Initialize recognizer
        self.recognizer = KaldiRecognizer(self.model, 16000)  # always use 16kHz for Vosk

    def get_input_device(self):
        print("Available audio input devices:")
        for idx, device in enumerate(sd.query_devices()):
            if device['max_input_channels'] > 0:
                print(f"[{idx}] {device['name']} - Input channels: {device['max_input_channels']}")
        # Select first real microphone containing "Microphone"
        for idx, device in enumerate(sd.query_devices()):
            if device['max_input_channels'] > 0 and "Microphone" in device['name']:
                samplerate = int(device['default_samplerate'])
                channels = device['max_input_channels']
                print(f"Auto-selected microphone: [{idx}] {device['name']} with {channels} channels")
                return idx, samplerate, channels
        raise RuntimeError("No valid microphone found.")

    def listen(self, duration=5):
        print(f"Listening on device {self.device_index}, channels {self.channels}, samplerate {self.samplerate}")
        try:
            recording = sd.rec(
                int(duration * self.samplerate),
                samplerate=self.samplerate,
                channels=self.channels,
                dtype='int16',
                device=self.device_index
            )
            sd.wait()
            print(f"Recording shape: {recording.shape}")

            # Convert to mono if stereo
            if recording.shape[1] > 1:
                recording = np.mean(recording, axis=1).astype(np.int16)
                print(f"Converted to mono shape: {recording.shape}")

            # Resample to 16kHz for Vosk
            if self.samplerate != 16000:
                number_of_samples = round(len(recording) * 16000 / self.samplerate)
                recording = resample(recording, number_of_samples).astype(np.int16)
                print(f"Resampled to 16kHz, shape: {recording.shape}")

        except Exception as e:
            print(f"Microphone error: {e}")
            return ""

        # Vosk recognition
        if self.recognizer.AcceptWaveform(recording.tobytes()):
            result = json.loads(self.recognizer.Result())
            text = result.get("text", "")
            if not text.strip():
                print("I heard nothing.")
            else:
                print(f"Raw heard text: {text}")
            return text
        else:
            partial = json.loads(self.recognizer.PartialResult())
            return partial.get("partial", "")
