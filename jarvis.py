from calendar import month
from email.mime import audio
from re import M, search
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import smtplib
import os
import subprocess as sp
import requests


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
    Time=datetime.datetime.now()
    speak(f"the time is {Time}")
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def date():
    date=datetime.datetime.now().strftime("%D")
    month=datetime.datetime.now().strftime("%M")
    year=datetime.datetime.year
date()
def wishes():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak(f"good morning {name}")
    elif hour >=12 and hour <18:
        speak(f"good evenig {name}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio ,language='en-US')
        if not 'goodbye' in query or 'shut up' in query:
            speak("i cant hear you sir")
        if 'okay' in query:
            pass
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
    speak(f"what do you want to search on wikipedia {name}")
    search=takeCommand().lower()
    results=search_wikipedia(query)
    results=wikipedia.summary(query,sentences=2)
    speak(f"according to wikipedia{results}")
    return results

def google(query):
    speak(f'what do you wanta to search on google{name}')
    search=takeCommand().lower()
def sendmail(to,content):
    email='jamesbengi21@gmail.com'
    password='Jemo1999'
    speak('Who do you want to send mail to')
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    server.sendmail(email,to,content)
    server.close()
NEWS_API_KEY ='743465dc458143aa816706415c58b57e'


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
        speak(f"here are the latest news{news_headlines}")
    return news_headlines[:5]
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    speak('im on it sir')
    return res["joke"]
if __name__ == "__main__":
    wishes()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            search_wikipedia()
        elif 'youtube' in query:
            play_on_youtube()
        elif 'send email' in query:
            sendmail()
        elif 'time' in query:
            time()
        elif 'camera' in query:
            open_camera()
        elif 'news' in query:
            get_latest_news()
        elif 'jokes' in query:
            get_random_joke()
        elif 'bye' in query:
            exit()
        




    