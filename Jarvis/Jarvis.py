import pyttsx3 # text data into speach
import datetime # waktu
import speech_recognition as sr # input command dari mic
import smtplib # kirim email
from credential import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as web #web browser untuk membuka wa
from time import sleep
import wikipedia # pencarina wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak('Hello, this is Jarvis')
        
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak('hello, this is Friday')

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #jam = I, Menit = M, detik = S
    speak("the current time is: ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('the current date is: ')
    speak(day)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <11:
        speak('good morning')
    elif hour >= 11 and hour < 18:
        speak('good afternoon')
    elif hour >= 18 and hour < 24:
        speak('good evening')
    else:
        speak('good night your majesty')

def wishme():
    speak('welcome back Lord!')
    time()
    date()
    speak('Friday at your service, please tell me how can i help you?')

def takeCommandCMD():
    query = input('please tell me how can i help you? ')
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again please my lord')
        return 'none'
    return query

def sendEmail(receiver,subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['from'] = senderemail
    email['to'] = receiver
    email['subject'] = subject
    server.set_content(content)
    server.send_message
    server.close()
    
def sendWhatsmsg(phone_num, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_num+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    web.open('https://www.google.com/search?q='+search)
    
def news():
    newsapi = NewsApiClient(api_key='your api')
    speak('what topic do you want to hear about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
        
    speak("that's it for now i'll update you in sometime")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def screenshot():
    name_img = tt.time()
    name_img = f'D:\\Documents\\Python - Udemy Course\\Jarvis\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()
    
def passwordgen():
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

if __name__ == "__main__":
    getvoices(2)
    # wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {
                'testemail' : 'test@gmail.com'
            }
            try:
                speak('to who you want to send the email?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak('what is the subject of the mail?')
                subject = takeCommandMic()
                speak('what should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak('email has been sended')
            except Exception as e:
                print(e)
                speak('unable to send the email')
        elif 'message' in query:
            user_name = {
                'Friday' : '+62 877 3062 3410'
            }
            try:
                speak('to who you want to send the whatsapp message?')
                name = takeCommandMic()
                phone_num = user_name[name]
                speak('what is the message?')
                message = takeCommandMic()
                sendWhatsmsg(phone_num, message)
                speak('whatsapp message has been sended')
            except Exception as e:
                print(e)
                speak('unable to send the whatsapp message')
        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'search' in query: 
            searchgoogle()
        elif 'youtube' in query:
            speak('what should i search for on youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
        elif 'news' in query:
            news()
        elif 'read' in query:
            text2speech()
        elif 'open code' in query:
            codepath = 'C:\\Users\\iwana\\OneDrive\\Dokumen\\Desktop\\Visual Studio Code.lnk'
            os.startfile(codepath)
        elif 'open explorer' in query:
            codepath = 'explorer C://{}'.format(query.replace('Open', ''))
            os.startfile(codepath)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'screenshot' in query:
            screenshot()
        elif 'remember' in query:
            speak('what should i remember?')
            data = takeCommandMic()
            speak('you told me to remember that'+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you told me to remember that '+remember.read())
        elif 'password' in query:
            passwordgen()
        elif 'offline' in query:
            speak('as you wish lord')
            quit()
            
            