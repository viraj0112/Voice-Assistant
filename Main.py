
from distutils.log import error
from unittest import result
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia,os


myName = "nisarga's assistant"
#sapi5-microsoft assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <= 12:
        speak("good morning nouman")
    elif hour > 12 and hour < 18:
        speak('good afternoon nouman')
    else:
        speak("good evening nisarga")
    speak(f'I AM {myName} , HOW MAY I HELP YOU?')


def hearme():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("listening....")
        r.adjust_for_ambient_noise(source)
           

        speak('yess listening')
        audio = r.listen(source)
    try:
        speak('recognizing your command')  # speak
        query = r.recognize_google(audio,language='en-in')
        # query="youtube"
        print(query)
        speak(query)
        # r.pause_threshold=1     
        
            
        if 'wikipedia' in query.lower():
            speak('Searching wiki....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary('query1',sentence=2)
            speak("Wiki result...")
            speak(query)
            print(results)
            speak(results)
            webbrowser.open("wikipedia.org/wiki/Main_Page")

        elif "youtube" in query.lower():
            
            # print(results)
            # speak(results)
            webbrowser.open("www.youtube.com")            
            # os.system("start chrome youtube.com")
            
# function 1
        elif "notes" or "notepad" in query.lower():
            
            # print(results)
            # speak(results)
            os.system("notepad")
    

    except Exception as error:
        print(error)
        speak('say that again, please')  # speak
        return None

def foo():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("listening....")
        r.adjust_for_ambient_noise(source)
           

        speak('yess listening')
        audio = r.listen(source)
    try:
        speak('recognizing your command')  # speak
        query1 = r.recognize_google(audio,language='en-in')
        # query="youtube"
        print(query1)
        speak(query1)
        # r.pause_threshold=1

        if query1.startswith(query1) :     
            speak(f"{query1} opening in browser")
            # result=query1.split(" ")
            
            webbrowser.open(f"{query1}.com")
            # os.system(f"start chrome {query1}.com")

        

            
    except Exception as error:
        print(error)
        speak('say that again, please')  # speak
        return None

# mic_list = sr.Microphone.list_microphone_names()
# print(mic_list)

if __name__ == "__main__":
    # wishme()
    # hearme()
    
    foo()

