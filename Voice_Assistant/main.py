import datetime
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Travis Sir. Please tell me how may I assist you today?.")


def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except:
        print("Say that again please..")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Lenovo\\Music\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourgmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except:
                speak("Sorry my friend. I am not able to send this email.")

        elif 'joke' in query:
            jokes = pyjokes.get_joke(language='en', category='neutral')
            speak(jokes)
        elif 'exit' in query:
            speak("Thank you!I'm happy to assist you.")
            break

        time.sleep(10)
