import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import wikipedia
import calendar
import requests
from bs4 import BeautifulSoup as bs

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"

session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    k=datetime.now()
    kk=int(k.hour)
    if kk>=0 and kk<=12:
        speak("Good Morning!")
    elif kk>12 and kk<=16:
        speak("Good Afternoon!")
    elif kk>16:
        speak("Good Evening!")

try:
    r=sr.Recognizer()
    d=sr.Microphone(device_index=0)
    with d as source:
        greet()
        speak("I am Kashikoi...How may I help you?")
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        m=r.listen(source)
    i=r.recognize_google(m)
except:
    print("Could not hear! Please speak again..")

try:
    def questions(i):
        if "your name" in i.lower():
            speak("My friends call me Kashikoi..")
        
        elif ("hello" or "hi") in i.lower():
            speak("Hello...Nice to hear you!")
        
        elif "how are you" in i.lower():
            speak("I am fine, thank you...Hope you are doing good too...")
    
        elif "call you" in i.lower():
            speak("You can call me Kashikoi..")
        
        elif "who are you" in i.lower():
            speak("Hey, I am Kashikoi.. I am your voice assistant created by Dhanashri Prakash...")

        elif "bye" in i.lower():
            speak("Bye...Take care! See you again...")
        
        elif ("who made you" or "who created you") in i.lower():
            speak("Thanks to Dhanashri Prakash who made me!!")

        elif "date" in i.lower():
            dd=datetime.now()
            rd={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            ddd=dd.day
            dr=dd.month
            print("Today's date is "+str(ddd)+" "+rd[dr])
            speak("Today's date is "+str(ddd)+rd[dr]) 
          
        elif "month" in i.lower():
            rd={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            dd=datetime.now()
            ddd=dd.month
            print("Current month is",rd[ddd])
            speak("Current month is "+(rd[ddd]))

        elif ("weekday" or "day") in i.lower():
            z=datetime.now()
            qq=z.year
            drd=z.month
            qw=z.day
            rd={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
            dd=calendar.weekday(qq,drd,qw)
            print("Today is",rd[dd])
            speak("Today is "+rd[dd])

        elif "time" in i.lower():
            z=datetime.now().strftime("%I:%M %p")
            print("Its "+z)
            speak("Its"+z)

    questions(i)

    def action(i):
        if "google" in i.lower():
            print("Opening Google...")
            speak("Opening Google")
            url="google.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "youtube" in i.lower():
            print("Opening Youtube...")
            speak("Opening youtube")
            url="youtube.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "whatsapp" in i.lower():
            print("Opening Whatsapp...")
            speak("Opening Whatsapp")
            url="web.whatsapp.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif ("gmail" or "email") in i.lower():
            print("Opening Gmail...")
            speak("Opening gmail")
            url="mail.google.com/mail/u/0/#inbox"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "wikipedia" in i.lower():
            print("Searching on Wikipedia...")
            speak("searching on wikipedia")
            rk=copy(i)
            rk.replace("Wikipedia"," ")
            result=wikipedia.summary(rk,3)
            print(result)
            speak(result)
        
        elif "geeks" in i.lower():
            print("Opening GeeksforGeeks...")
            speak("Opening geeksforgeeks")
            url="geeksforgeeks.org"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "github" in i.lower():
            print("Opening Github...")
            speak("Opening Github")
            url="github.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "linkedin" in i.lower():
            print("Opening LinkedIn...")
            speak("Opening linkedin")
            url="linkedin.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "read news" in i.lower():
            print("Reading today's headlines...")
            speak("Reading today's headlines")
            ll="latest news"
            url="https://www.hindustantimes.com/"+ll
            html = session.get(url)
            soup= bs(html.text,"html.parser")
            mm=soup.find_all("h3",attrs={"class":"hdg3"})
            for ele in mm:
                rr=ele.text
                print(rr)
                speak(rr)
            print("That's all for today...")
        
        elif "w3school" in i.lower():
            print("Opening w3schools...")
            speak("Opening w3schools")
            url="w3schools.com"
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(path).open(url)

        elif "open news" in i.lower():
            abc=i.replace("open","latest")
            print("Opening latest news...")
            speak("Opening latest news")
            webbrowser.open(abc)
        
        elif "temperature" in i.lower():
            url="https://www.google.com/search?q="+i
            html=session.get(url)
            soup=bs(html.text,"html.parser")
            temp = soup.find("span", attrs={"id": "wob_tm"}).text
            e="Temperature feels like "+temp+"°Celcius"
            print(e)
            speak(e)
        
        elif ("weather forecast" or "weather details") in i.lower():
            print("Showing Weather Forecast...")
            speak("Showing weather forecast")
            webbrowser.open(i)
        
        elif "weather" in i.lower():
            print("Fetching weather updates...")
            speak("Fetching weather updates")
            url="https://www.google.com/search?q="+i
            html=session.get(url)
            soup=bs(html.text,"html.parser")
            wea = soup.find("span", attrs={"id": "wob_dc"}).text
            d="Weather is "+wea
            print(d)
            speak(d)
        
        elif "search" or "play" in i.lower():
            if "search" in i.lower():
                pp=i.replace("search","")
                print("Searching"+pp)
                speak("Searching"+pp)
                webbrowser.open(pp)
            
            elif "play" in i.lower():
                pp=i.replace("play","")
                print("Playing"+pp)
                speak("Playing"+pp)
                webbrowser.open(pp)

    action(i)
except:
    print("An error occured! Please try again..")

