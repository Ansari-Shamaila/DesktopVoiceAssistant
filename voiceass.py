import sys
from sys import argv
import subprocess as sp
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from voiceassistant import Ui_voiceassistant


import pyttsx3  # TO CONVERT TEXT DATA INTO SPEECH
import datetime
import speech_recognition as sr  # Speech from microphone to text
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
# from newsapi import NewsApiClient
import os
import pyjokes
import time as tt
import string
import random
import psutil  # for cpu and battrey
import subprocess as sp



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime(
        "%I:%M:%S")  # hour=I,minutes=M,Seconds=S
    speak("The current time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Todays date is:")
    speak(date)
    speak(month)
    speak(year)
# date()


def greeting():
    # tells us hour so that accordingly he can greet us
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night!")


def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service,please tell me how can i help you?")


def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')



#def Insta():
    
 #   wb.open('https://www.instagram.com/?hl=en'+search)

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution(self)

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    def TaskExecution(QThread, self):
        wishme()
        while True:
            # if 1:
            self.query = self.takeCommand().lower()

        # Logic for executing tasks based on query

            if 'time' in self.query:
                time()

            elif 'date' in self.query:
                date()
            elif 'message' in self.query:
                user_name = {
                    'Neha': '8657646754',
                    'Tina': '7499976543',
                    'Veda': '9096169086'


                }
                try:
                    speak("To whom you want to send the whatsapp message? ")
                    name = self.takeCommand()
                    phone_no = user_name[name]
                    speak("what is the message?")
                    message = self.takeCommand()
                    sendwhatsmsg(phone_no, message)
                    speak("message has been said")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")

            elif 'wikipedia' in self.query:
                speak('searching on wikipedia...')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            elif 'search ' in self.query:
                speak('What should i search for?')
                search = self.takeCommand()
                wb.open('https://www.google.com/search?q='+search)

            elif 'youtube' in self.query:
                speak("What Should i search on youtube?")
                topic = self.takeCommand()
                pywhatkit.playonyt(topic)

            elif 'weather' in self.query:

                city = 'Mumbai'

                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=0e5a0060fe4566aae319488a7f6856ff'

                res = requests.get(url)
                data = res.json()

                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                desp = data['weather'][0]['description']
                temp = round((temp-32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in {city} city is like')
                speak('Temperature :{} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))

            # elif 'news' in self.query:
            #     newsapi = NewsApiClient(
            #         api_key='3b3bcca828da4154adc378753b7f96ad')  # connect with api
            #     speak('On what topic you need the news ?')
            #     topic = self.takeCommand()
            #     data = newsapi.get_top_headlines(q=topic,
            #                                      language='en',
            #                                      page_size=5)  # get the data about bitcoin in english language

            #     newsdata = data['articles']

            #     for x, y in enumerate(newsdata):
            #         print(f'{x}{y["description"]}')
            #         speak((f'{x}{y["description"]}'))
            #     speak("That's it for now i'll update you in sometime")

            # open document
            elif 'open' in self.query:
                os.system(
                    'explorer C://{}'.format(self.query.replace('Open', '')))

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif 'screenshot' in self.query:
                name_img = tt.time()
                name_img = f'screenshot{name_img}.png'
                img = pyautogui.screenshot(name_img)
                img.show()

            elif 'password' in self.query:
                s1 = string.ascii_uppercase
                s2 = string.ascii_lowercase
                s3 = string.digits
                s4 = string.punctuation

                passlen = 8
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))

                random.shuffle(s)
                newpass = ("".join(s[0:passlen]))
                print(newpass)
                speak(newpass)

            elif 'cpu' in self.query:
                usage = str(psutil.cpu_percent())
                speak('CPU is at'+usage)
                battery = psutil.sensors_battery()
                speak("Battery is at")
                speak(battery.percent)
            elif 'open code' in self.query:
                codepath = 'C:\\Users\\Ansari Hunen\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
                os.startfile(codepath)

            elif 'play music' in self.query or "play song" in self.query or "song" in self.query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = r"C:\Users\Ansari Hunen\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'shutdown' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

            elif "restart" in self.query:
                sp.call(["shutdown", "/r"])

            elif 'instagram' in self.query:
                speak("Opening Instagram")
                wb.open("instagram.com")

            elif 'camera' in self. query:
                sp.run('start microsoft.windows.camera:', shell=True)

            elif 'remember that' in self.query:
                speak("What should i remember?")
                data = self.takeCommand()
                speak("You said me to remember that"+data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in self.query:
                remember = open('data.txt', 'r')
                speak("You told me to remember that"+remember.read())

            elif 'offline' in self.query:
                quit()


startExecution = MainThread()


class Main(QMainWindow, Ui_voiceassistant):
    def __init__(self):
        super().__init__()
        self.ui = Ui_voiceassistant()
        self.ui.setupUi(self)
        self.ui.push_run.clicked.connect(self.startTask)
        self.ui.push_exit.clicked.connect(self.close)

    def startTask(self):

        startExecution.start()


app = QApplication(sys.argv)
Va = Main()
Va.show()
exit(app.exec_())
