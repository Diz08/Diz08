import streamlit as st
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os

# Function to generate a sound wave and give it a frequency
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave 

# Function to save the generated wave as temporary file
def save_wave(wave, sample_rate=44100): 
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    write(temp_file.name, sample_rate, wave)
    return temp_file

# Function to play the generated sound
def play_sound(note_freq):
    wave = generate_sine_wave(note_freq, duration=1.0)
    temp_wav_file = save_wave(wave)
    st.audio(temp_wav_file, format='audio/wav')
    os.remove(temp_wav_file)

#Frequency of piano keys 
piano_keys = {
    'C': 261.63, 
    'D': 293.66,
    'E': 329.63, 
    'F': 349.23, 
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}
 
st.title('DizBalls')

# Create piano key buttons
for note, freq in piano_keys.items():
    if st.button(note):
        play_sound(freq)




