import pyttsx3 # text data into speach
import datetime # waktu
import speech_recognition as sr # input command dari mic

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        
    speak('aaah sayang')

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
    speak('Jarvice at your service, please tell me how can i help you?')

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

if __name__ == "__main__":
    # wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()


# # getvoices()
# while True:
#     voice = int(input('press 1 for male voice\npress 2 for female voice\ninput: '))
#     getvoices(voice)