import speech_recognition as sr
import  webbrowser as wb
import pyaudio


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()


with sr.Microphone() as source:
    print('search youtube by saying video')
    print('speak now')
    audio = r3.listen(source)
    g = r2.recognize_google(audio)
    print(g)

if 'video' in r2.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search what you want on you tube!')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('faild'.format(e))

