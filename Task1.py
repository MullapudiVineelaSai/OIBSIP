import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I didn't catch that. Please say again.")
        return ""

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you?")

if __name__ == "__main__":
    wish()
    while True:
        query = take_command()
        
        if "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
            
        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
            
        elif "google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
            
        elif "stop" in query or "exit" in query:
            speak("Okay, Goodbye!")
            break
            
        elif query != "":
            speak("I can tell time, open youtube, or open google. What else?")