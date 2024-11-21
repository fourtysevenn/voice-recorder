import sounddevice as sd
import wavio as wv



audioname=input("Give your audio a name (include .wav extension, e.g. 'my_audio.wav'):  ")
print("This program just gives you 5 minutes to record..")
if not audioname.endswith('.wav'):
    audioname += '.wav'

duration=int(input("Give your record duration in seconds.."))



def voicerecord():
    freq = 44100



    recording = sd.rec(int(freq * duration), samplerate=freq, channels=2)
    sd.wait()


    wv.write(audioname, recording, freq, sampwidth=2)


voicerecord()








