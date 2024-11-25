import sounddevice as sd
import numpy as np
import wavio

def record_audio(duration, samplingFrequency, filename):
    print("Recording...")
    audio = sd.rec(int(duration * samplingFrequency), samplerate=samplingFrequency, channels=1, dtype='int16')
    sd.wait() 
    print("Recording complete!")
    wavio.write(filename, audio, samplingFrequency, sampwidth=2)
    print(f"Saved to {filename}")

samplingFrequency = 16000
duration = 10  
filename = "input3.wav"

record_audio(duration, samplingFrequency, filename)
