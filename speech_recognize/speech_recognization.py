#import required library
import speech_recognition as sr
import  webbrowser as wb
import pyaudio

#create instance of speech_recognition 
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

#taking input voice from microphone
with sr.Microphone() as source:
    print('search youtube by saying video')
    print('speak now')
    audio = r3.listen(source)
    #convert voice into text
    g = r2.recognize_google(audio)
    print(g)
#if you say video then
if 'video' in r2.recognize_google(audio):
    r1 = sr.Recognizer()
    #you tube url to search given query
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search what you want on you tube!')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            #open web page of search query on you tube 
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('faild to get result'.format(e))

