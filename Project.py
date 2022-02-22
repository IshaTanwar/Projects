import pyttsx3 #text-speech conversion library
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import smtplib

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 250)     # setting up new voice rate

#visit =	{
#  "google": "https://www.google.com/?client=safari",
#  "youtube": "https://www.youtube.com",
#  "episode": "https://biggbossserial.com"
#}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mam, How can I help you")
    elif hour<=12 and hour<18:
        speak("Good Afternoon Mam, How can I help you")
    else:
        speak("Good Evening Mam, How can I help you")

def takeCommand():
    '''
    Purpose: convert speech to text
    Input: Microphone input from user
    Output: Returns string
    '''
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ishaskib@gmail.com', 'mypasswordisstrong')
    server.sendmail('ishaskib@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    engine.setProperty('rate', 200)
    wishMe()

    while True:
        query = takeCommand().lower()
        #for key in visit:
        #    if key in query:
        #        word = key
        #        link = visit[key]
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/?client=safari")

        elif 'episode' in query:
            webbrowser.open("https://biggbossserial.com")

        #elif word in query:
        #    webbrowser.open(link)

        elif 'open uvic website' in query:
            webbrowser.open("https://www.uvic.ca/tools/index.php")

        elif 'open brightspace' in query:
            webbrowser.open("https://bright.uvic.ca/d2l/home")

        elif 'boring day song' in query:
            webbrowser.open("https://youtu.be/UiiqUL0Adfc")
            break
            

        elif 'bigg boss 13' in query:
            pywhatkit.playonyt("shehnaaz unseen undekha")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"Mam, the time is {strTime}")

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("The date is %d,%B,%Y and the day is %A")    
            print(strTime)
            speak(f"Mam, the date is {strTime}")

        elif 'email to isha' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ishaskib@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Isha. I am not able to send this email")    

        elif 'thank you' in query:
            speak("It's my pleasure to help you. You are always welcome!")
            break

        elif 'how are you' in query:
            speak("I am amazing Mam. How about you?")