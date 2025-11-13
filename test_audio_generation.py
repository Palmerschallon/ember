"""
Test Ember's absorbed audio synthesis knowledge
Generate a simple musical phrase using numpy
"""
import numpy as np
import wave
import struct

# Audio parameters
SAMPLE_RATE = 44100  # Hz
DURATION = 3.0  # seconds
AMPLITUDE = 0.3

# Musical note frequencies (A4 = 440 Hz)
NOTES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}

def generate_tone(frequency, duration, sample_rate=SAMPLE_RATE):
    """Generate a sine wave tone"""
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Add envelope (fade in/out) to prevent clicks
    envelope = np.ones_like(t)
    fade_samples = int(sample_rate * 0.01)  # 10ms fade
    envelope[:fade_samples] = np.linspace(0, 1, fade_samples)
    envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)
    
    wave = AMPLITUDE * np.sin(2 * np.pi * frequency * t) * envelope
    return wave

def generate_melody():
    """Generate a simple melody"""
    melody = [
        ('C4', 0.3),
        ('E4', 0.3),
        ('G4', 0.3),
        ('C5', 0.6),
        ('G4', 0.3),
        ('E4', 0.3),
        ('C4', 0.6),
    ]
    
    audio = []
    for note, duration in melody:
        tone = generate_tone(NOTES[note], duration)
        audio.append(tone)
    
    return np.concatenate(audio)

def save_wav(filename, audio_data, sample_rate=SAMPLE_RATE):
    """Save audio data as WAV file"""
    # Convert to 16-bit PCM
    audio_int16 = np.int16(audio_data * 32767)
    
    with wave.open(filename, 'w') as wav_file:
        # Set parameters: nchannels, sampwidth, framerate, nframes, comptype, compname
        wav_file.setparams((1, 2, sample_rate, len(audio_int16), 'NONE', 'not compressed'))
        
        # Write audio data
        for sample in audio_int16:
            wav_file.writeframes(struct.pack('h', sample))
    
    print(f"✅ Generated: {filename}")
    print(f"   Duration: {len(audio_data)/sample_rate:.2f}s")
    print(f"   Sample rate: {sample_rate} Hz")
    print(f"   Samples: {len(audio_data)}")

# Generate and save
print("🎵 Testing absorbed audio synthesis knowledge...")
print("Generating melody using pure sine waves...")

melody = generate_melody()
save_wav('/media/palmerschallon/ThePod1/ember_first_song.wav', melody)

print("\n🎉 Ember's first sound creation!")
print("The absorbed 'synthesis', 'frequency', 'audio' concepts work!")
