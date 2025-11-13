import numpy as np
import sounddevice as sd
import cv2

# Generate visual from audio
def audio_to_visual(audio):
    spectrum = np.fft.fft(audio)  
    spectrum = np.abs(spectrum[:len(spectrum)//2])
    
    width = len(spectrum)
    height = 480
    
    img = np.zeros((height, width, 3), np.uint8)
    
    for i, amp in enumerate(spectrum):
        hue = int(i/width * 180)
        sat = int(amp/np.max(spectrum) * 255)
        val = 255
        color = cv2.cvtColor(np.uint8([[[hue,sat,val]]]), cv2.COLOR_HSV2BGR)[0][0]
        color = (int(color[0]), int(color[1]), int(color[2]))
        cv2.line(img, (i,height), (i,height-int(amp/np.max(spectrum)*height)), color, 1)
        
    return img

# Generate audio from visual
def visual_to_audio(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    signal = np.mean(gray, axis=0)
    audio = np.fft.ifft(signal).real
    audio = audio.astype(np.int16)
    return audio

# Audio-visual feedback loop
def audio_visual_feedback(duration=10):
    sample_rate = 44100
    audio_buffer = np.random.uniform(-1, 1, sample_rate) 
    
    for i in range(duration):
        visual = audio_to_visual(audio_buffer)
        cv2.imshow('Visualization', visual)
        cv2.waitKey(1)
        
        audio = visual_to_audio(visual)
        audio_buffer = np.concatenate((audio_buffer[len(audio):], audio))
        
        sd.play(audio_buffer, sample_rate)

audio_visual_feedback()