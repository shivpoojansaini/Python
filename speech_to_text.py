#importing speech_recognition  library
import speech_recognition as sr
#creating instance of speech_recognition
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
# Taking input from microphone
with sr.Microphone() as source:
    print('speak now')
    #store listen voice in audio
    audio = r3.listen(source)
    #converting voice in text
    g = r2.recognize_google(audio)
    #printing listen voice
    print("you say!")
    print(g)



