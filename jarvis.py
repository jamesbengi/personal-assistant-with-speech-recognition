from calendar import month
from email.mime import audio
from re import M, search
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
engine=pyttsx3.init()
name="james"
bot="nicky"
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak(f"hello{name} my name is{bot}")

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {Time}")
time()
def date():
    date=datetime.datetime.now().strftime("%D")
    month=datetime.datetime.now().strftime("%M")
    year=datetime.datetime.year
date()
def wishes():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("good morning sir")
    elif hour >=12 and hour <18:
        speak("good evenig sir")
wishes()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio ,language='en-US')
        if not 'exit' in query or 'stop' in query:
            speak("i cant hear you sir")
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        print(query)
    except Exception :
        speak("say that again please")
        query="None"
    return query
takeCommand()
def play_on_youtube():
    speak('What do you want to play on Youtube, sir?')
    video = takeCommand().lower()
    kit.playonyt(video,use_api=True)

def search_wikipedia(query):
    speak(f"what do you want to search on wikipedia{name}")
    search=takeCommand().lower()
    results=search_wikipedia(query)
    results=wikipedia.summary(query,sentences=2)
    speak(f"according to wikipedia{results}")
    return results
search_wikipedia()
    