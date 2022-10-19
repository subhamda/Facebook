import pyttsx3
import speech_recognition as sr
from datetime import datetime
import datetime 
from datetime import date
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import time
import pyjokes


engine=pyttsx3.init('sapi5')     
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour  >= 0 and hour<12:
        speak("Good Morning sir")
    elif hour  >= 12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evenning sir")
    speak("I am your artificial intelligence and my name is jarvis")
    print("Loading your AI personal assistant, Please wait...")
    speak("Loading your AI personal assistant, Please wait....")
    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        speak("sorry, please say that again")
        print("Sorry, please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('arpitsinha472@gmail.com',to,content)
    server.close()

    
if __name__ == "__main__":
    wishMe()
    while True:
    
        speak("Tell me how can I help you now?")
        query=takeCommand().lower()
        if 'who are you' in query:
            speak('''I am your AI personal assistant and i can help you for doing some things like 
            search on wikipedia, open youtube , open google,
            open gmail, open stackoverflow, play music,
            show date and time,send email and open code ''')
            print('''I am your AI personal assistant and i can help you for doing some things like 
            search on wikipedia, open youtube , open google,
            open gmail, open stackoverflow, play music,
            show date and time,send email and open code ''')
            speak("how can i help you ?")
            
        if 'wikipedia' or 'who is'  in query:
            speak('Speaking wikipedia...')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print("According to wikipedia")
            print(results)
            speak(results)
            time.sleep(0.5)

        elif 'open youtube' in query:
            speak("youtube is opening now") 
            webbrowser.open_new_tab("https://www.youtube.com/")
            time.sleep(0.5)

        elif 'open google' in query:
            speak("Google chrome is opening now") 
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(0.5)
                                 
        elif 'open gmail' in query:
            speak("Google Mail open now")
            webbrowser.open_new_tab("gmail.com")
            time.sleep(0.5)
            
        elif 'open stackoverflow' in query:
            speak("stackoverflow is opening now")
            webbrowser.open_new_tab("https://stackoverflow.com/")
            time.sleep(0.5)
        

        elif 'play music' in query:
            music_dir ='D:\\New folder\\music'
            songs=os.listdir(music_dir)
            randno=random.randint(0,10)
            os.startfile(os.path.join(music_dir,songs[int(randno)]))
            time.sleep(0.5)

        
        elif 'date and time' in query:
            today=date.today()
            strTime = datetime.datetime.now().strftime("%H::%M::%S")
            d2= today.strftime("%B/ %m/ %Y")
            print(f"Today's date is :{d2}  Current time is: {strTime}")
            speak(f"Today's is {d2}")
            speak(f"and Current time is {strTime}")


        elif 'open code' in query:
            path="C:\\Users\\Arpit sinha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            time.sleep(0.5)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="arpitsinhaexpert@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am unable to send email.")
                time.sleep(0.5)
        
        elif 'jokes' in query:
            My_jokes = pyjokes.get_joke(language="en",category="neutral")
            print(My_jokes)
            speak(My_jokes)
            time.sleep(0.5)

        elif 'good bye' or 'stop' or 'exit' in  query:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            sys.exit(0)
       