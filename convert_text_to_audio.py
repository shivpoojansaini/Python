#import diffrent library for sound manuplation
from gtts import gTTS
from playsound import playsound
#function convert text into audio
def convert_to_audio(text):
    #coverting text in audio
    my_audio = gTTS(text)
    #save audio file as notface.mp3
    my_audio.save('notface.mp3')
#function to play mp3 file
def play_sound(audio_file):
    playsound(audio_file)
#function calling
convert_to_audio("sorry this is not a face! ")
play_sound('notface.mp3')
