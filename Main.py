
from distutils.log import error
from unittest import result
from winsound import PlaySound

from setuptools import Command
import speech_recognition as sr
import wikipedia, os, datetime, pyttsx3, webbrowser, keyboard, pyjokes
from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound 
import keyboard

myName = "nisarga's assistant"
# sapi5-microsoft assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(f"{myName} : {audio}")
    engine.runAndWait()


# def wishme():
#     hour = datetime.datetime.now().hour
#     if hour >= 0 and hour <= 12:
#         speak("good morning Thunder")
#     elif hour > 12 and hour < 18:
#         speak('good afternoon Thunder')
#     else:
#         speak("good evening Boult")
#     speak(f'I AM {myName} , HOW MAY I HELP YOU?')


def hearme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <= 12:
        speak("good morning Thunder")
    elif hour > 12 and hour < 18:
        speak('good afternoon Thunder')
    else:
        speak("good evening Boult")
    speak(f'I AM {myName} , HOW MAY I HELP YOU?')

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("listening....")
        # PlaySound("assistant_on.wav")
        r.adjust_for_ambient_noise(source)
           
        speak('yess listening')
        audio = r.listen(source)
        # PlaySound("assistant_off.wav")
    try:
        speak('recognizing your command')  # speak
        query = r.recognize_google(audio,language='en-in')
        print(query)
        # r.pause_threshold=1 
           
        
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

        elif query.lower().startswith('edit'):
            res = query.split()
            res = res[1:]
            res = " ".join(res)
            # for i in os.listdir("\Users\itse\Pictures"):
            for i in os.listdir("C:\\Users\\Viraj Sawant\\Pictures\\Screenshots"):
                if i.endswith((".jpeg", ".jpg", ".png")):
                    stmt = i.split(".")
                    if res == stmt[0].lower():
                        im = Image.open("C:\\Users\\Viraj Sawant\\Pictures\\Screenshots"+str(i))
                        filtered_image = im.filter(ImageFilter.BLUR)
                        im = Image.open("C:\\Users\\Viraj Sawant\\Pictures\\Screenshots"+ str(i))
                        filtered_image = ImageOps.grayscale(im)
                        filtered_image.save("edited_"+i, 'JPEG')
                        filtered_image.show()
                        print(i)
        

        elif query.lower() in ["kill", "quit", "stop", "exit"]:
            sys.exit(0)

    except Exception as error:
        print(error)
        speak('say that again, please')  # speak
        return None



def main_screen():
    global scr
    scr= Tk()
    scr.title("Thunder")
    scr.geometry("100x250")
    # scr.iconphoto("mic.png")

    name_label=Label(text="Thunder",width=300,bg="black",fg="white",font=("Calibri",13))
    name_label.pack()

    microphone_photo = PhotoImage(file = "mic.png")
    # microphone_button = Button(image=microphone_photo,command=wishme)
    microphone_button = Button(image=microphone_photo,command=hearme)
    microphone_button.pack(pady=10)

    image=Image.open("mic.png")
    resize_image=image.resize((20,30))
    img=ImageTk.PhotoImage(resize_image)
    label1=Label(image=img)
    label1.image=img
    label1.pack()


    settings_photo = PhotoImage(file = "setting.png")
    settings_button = Button(image=settings_photo)
    settings_button.pack(pady=50)

    info_button = Button(text ="Info")
    info_button.pack(pady=10)

    scr.mainloop()

    

keyboard.add_hotkey("F4",hearme)
main_screen()


if __name__ == "__main__":
    
    while True:
        # wishme()
        hearme()
    
   
   
