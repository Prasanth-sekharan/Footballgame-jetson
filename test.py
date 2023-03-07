import pyaudio
import numpy as np

def alert(frequency, duration):
    # Set parameters
    fs = 44100  # Sample rate
    seconds = duration  # Duration in seconds
    samples = int(fs * seconds)  # Number of samples

    # Generate waveform
    t = np.linspace(0, seconds, samples, False)  # Generate time array
    note = np.sin(frequency * t * 2 * np.pi)  # Generate sine wave

    # Play waveform
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(note.astype(np.float32).tobytes())
    stream.close()
    p.terminate()

# Example usage: play 440 Hz tone for 1 second
alert(2200, 2)
