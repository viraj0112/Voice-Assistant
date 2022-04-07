import pyttsx3, webbrowser
import datetime, os, sys
import speech_recognition as sr
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

myName = "Sky assistant"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <= 12:
        speak("good morning Sir")
    elif hour > 12 and hour < 18:
        speak('good afternoon Sir')
    else:
        speak("good evening Sir")
    speak(f'I AM {myName} , HOW MAY I HELP YOU?')


def hearme():
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source)

    #     speak('yess listening')
    #     audio = r.listen(source)
    try:
        speak('recognizing your command')  # speak
        # query = r.recognize_google(audio)
        query = input(">")
        print(query)

        # Open websites
        if query.lower().startswith("open") and "." in query.lower():
            res = query.split()
            print(res[1:])
            res = res[1:]
            webbrowser.open(f"{' '.join(res)}")

        # Open applications
        elif query.lower().startswith("open"):
            res = query.split()
            print(res[1:])
            res = res[1:]
            os.system(f"start {' '.join(res).lower()}")            

        # Time pass
        elif 'google' in query.lower():
            os.system("firefox google.com")

        # Video playback
        # elif query.lower().startswith('play'):
            # res = query.split()
            # print(res[1:])
            # res = res[1:]
            # os.system(f"python ./main2.py {' '.join(res)}")

        # Image manipulation
        elif query.lower().startswith('edit'):
            res = query.split()
            res = res[1:]
            res = " ".join(res)
            # for i in os.listdir("\Users\itse\Pictures"):
            for i in os.listdir("\\Users\\itse\\Pictures"):
                if i.endswith((".jpeg", ".jpg", ".png")):
                    stmt = i.split(".")
                    if res == stmt[0].lower():
                        # im = Image.open("\Users\itse\Pictures\\"+str(i))
                        # filtered_image = im.filter(ImageFilter.BLUR)
                        im = Image.open("\\Users\\itse\\Pictures\\"+ str(i))
                        filtered_image = ImageOps.grayscale(im)
                        filtered_image.save("edited_"+i, 'JPEG')
                        filtered_image.show()
                        print(i)

        elif query.lower() in ["kill", "quit", "stop", "exit"]:
            sys.exit(0)

    except Exception as err:
        print(err)
        speak('say that again, please')  # speak
        return 'None'


if __name__== "__main__":
    wishme()
    while True:
        hearme()