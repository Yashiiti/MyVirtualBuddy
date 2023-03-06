import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import requests
import bs4
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("How may I assist you?")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(f"{e}\nPlease say that again.")
        return "None"

    return query.lower()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {strTime}")

        elif 'open code' in query:
            codepath = ("C:\\Users\\PURAV\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code")
            os.startfile(codepath)

        elif 'quit' in query or 'exit' in query or 'leave' in query:
            speak("Goodbye sir!")
            sys.exit()

        elif 'what can you do' in query or 'help' in query:
            speak('I can do multiple things like telling time, opening Google, YouTube, StackOverflow, Wikipedia, playing music, and more. How can I assist you, sir?')

        elif 'who are you' in query:
            speak('I am your personal assistant.')

        elif 'thank' in query:
            speak("You're always welcome, sir.")

        elif 'write' in query or 'type' in query:
            if 'write' in query:
                word = 'write'
            elif 'type' in query:
                word = 'type'
            write=query.replace(word,'')
            for char in write:
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.12)
        elif 'setting' in query or 'settings' in query:
            speak('Opening settings')
            keyboard.press(Key.cmd)
            keyboard.press('i')
            keyboard.release(Key.cmd)
            keyboard.release('i')
        elif 'morning' in query or 'afternoon' in query or 'evening' in query:
            wishMe()
        elif 'close' in query:
            keyboard.press(Key.alt_l)
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.alt_l)
        elif 'notepad' in query:
            codepath=("C:\\Users\\PURAV\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
            os.startfile(codepath)
            
        speak('Thank You for using me Sirr') 
