import sounddevice as sd

duration = 5  # seconds
device_index = 15  # your real mic
device_info = sd.query_devices(device_index, 'input')
samplerate = int(device_info['default_samplerate'])
channels = min(2, device_info['max_input_channels'])

print("Recording...")
recording = sd.rec(int(duration * samplerate),
                   samplerate=samplerate,
                   channels=channels,
                   dtype='int16',
                   device=device_index)
sd.wait()
print("Recording complete. Your microphone is working!")
