import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import wolframalpha
import smtplib
import time
import json
import random
import PyDictionary
import googlesearch
from urllib.request import urlopen 
from googlesearch import search
from PyDictionary import PyDictionary
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    #speak("Samarjeet.............")

    speak("I am Darvin,Sir. Please tell me how may I help you.")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
    server.ehlo()
    server.starttls()
    server.login('samarjeetdeo007@yahoo.com', 'Samar@007')
    server.sendmail('samarjeetdeo007@yahoo.com', 'samarjeetdeo007@gmail.com', content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Samarjeet said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

dictionary=PyDictionary()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for execution of task based on query
        if 'wikipedia' in query or 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("who is", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print("Darvin:")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry my friend.... I am not able to search rite now...Check your input or try again")

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'meaning' in query:
            speak('Searching meaning...')
            try:
                query = query.replace("meaning", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print("Darvin:")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry my friend.... I am not able to search rite now...")

        elif 'dictionary' in query:
            speak("Say the word you want to search")
            word = takeCommand().lower()
            try:
                # dictionary=PyDictionary()
                print(word)
                speak(word)
                sol = (dictionary.meaning(word))
                print(sol)
                speak(sol)
            except Exception as e:
                print(e)
                speak("Sorry my friend.... I am not able to search rite now...")

        elif "who made you" in query or "who created you" in query:
            print("Darvin: I was made by Mr. Samarjeet.")
            speak("I was made by Mr. Samarjeet.")

        elif 'joke' in query: 
            speak(pyjokes.get_joke())

    

        # elif "write a note" in query: 
        #     speak("What should i write, sir") 
        #     note = takeCommand() 
        #     file = open('darvin.txt', 'w') 
        #     speak("Sir, Should i include date and time") 
        #     snfm = takeCommand() 
        #     if 'yes' in snfm or 'sure' in snfm: 
        #         strTime = datetime.datetime.now().strftime("% H:% M:% S") 
        #         file.write(strTime) 
        #         file.write(" :- ") 
        #         file.write(note) 
        #     else: 
        #         file.write(note) 
          
        # elif "show note" in query: 
        #     speak("Showing Notes") 
        #     file = open("darvin.txt", "r")  
        #     print(file.read()) 
        #     speak(file.read(6))

        # elif 'search' in query:  
        #     query = query.replace("search", " ")            
        #     webbrowser.open(query)

        elif "don't listen" in query or "stop listening" in query: 
            speak("For how much time you want to stop me from listening commands")
            try: 
                a = int(takeCommand()) 
                time.sleep(a) 
                print(a)
            except Exception as e:
                print(e)
                speak("Sorry my friend.... I am not able to search rite now...")

        elif "calculate" in query:        
            app_id = 'QE4ETK-96EA2WAXA5' 
            client = wolframalpha.Client(app_id) 
            try:
                indx = query.lower().split().index('calculate')  
                query = query.split()[indx + 1:]  
                res = client.query(' '.join(query))  
                answer = next(res.results).text 
                print("Darvin: The answer is " + answer)  
                speak("The answer is " + answer)
            except Exception as e:
                print(e)
                speak("Kindly Check your input")

        elif "what is" in query: 
            client = wolframalpha.Client('QE4ETK-96EA2WAXA5') 
            res = client.query(query)     
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except Exception as e: 
                print ("No results") 

        
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            try:
                webbrowser.open("https://www.google.com/maps/place/" + location + "")
            except Exception as e:
                print(e)
                speak("Kindly Check your input")


        elif 'thank you' in query:
            speak("Welcome sir,I am always there for you sir")

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query: 
            speak("It's good to know that your fine") 

        elif 'who are you' in query:
            speak("I am Darvin sir. A initial stage of A I speech recognition system.")
            
        elif 'about yourself' in query:
            speak("I am Darvin sir. A initial stage of A I speech recognition system.")
            speak("I work on basic commands at current stage")
            speak("But I am sure I will be able to do a lot in future")
            speak("Rest part I cannot say right now as its confidencial")
            speak("Currently my response time is not upto mark but my developers are working on it")
            speak("Will surely meet in future with many new aspects")
            speak("Thank You,hope you liked me")

        elif 'i like you' in query:
            print("Darvin: I like you too..")
            speak("hahahahahaha... its great i like you too.....")
            speak("Who tells AI don't have feelings.......")
            speak("I do have......")
            speak("I also adorable and I like getting love from you....... ")

        elif 'i love you' in query:
            print("Darvin: I love you too")
            speak("I love you too")
            speak("But my bad luck that I am a AI")
            speak("If was a human i surely would have fallen for you..")

        elif "will you be my gf" in query or "will you be my girlfriend" in query or "will you be my boyfriend" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time")

        elif 'open college website' in query:
            speak("Opening college website")
            webbrowser.open("www.cutm.ac.in")
        
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("playing music")
            music_dir = 'F:\\Songs'
            a = random.randint(1,67)
            Songs = os.listdir(music_dir)
            #print(Songs)
            os.startfile(os.path.join(music_dir, Songs[a]))

        elif 'play songs' in query:
            speak("playing songs")
            music_dir = 'F:\\Songs'
            a = random.randint(1,67)
            Songs = os.listdir(music_dir)
            #print(Songs)
            os.startfile(os.path.join(music_dir, Songs[a]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Darvin:")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            codePath = "C:\\Users\\DecentDevil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "samarjeetdeo007@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Samarjeet.... I am not able to send this email...")

        elif 'tell me a story' in query:
            speak("Playing a story")
            music_dir = 'F:\\Short stories'
            Songs = os.listdir(music_dir)
            #print(Songs)
            os.startfile(os.path.join(music_dir, Songs[0]))

        elif 'sing a song' in query:
            speak("Sorry I initially cannot sing a song but play a song for you")
            speak("Try Saying... Darvin Play songs")

        elif 'experiments' in query:
            speak("Opening AI Experiments")
            webbrowser.open("https://experiments.withgoogle.com/collection/ai")

        elif 'search' in query:
            speak("Say what you wanna search")
            query = takeCommand().lower()
            #iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
            #firefoz_path = r'D:\SoftwareInstalled\Firefox\firefox.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'weather forecast' in query:
            speak("Searching about whether forecast")
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
        
        elif 'latest news' in query:
            speak("Searching about latest news")
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            speak("Please select from the following links on the screen, I have listed some links of some websites on the screen. Thank you")

        elif 'goodbye' in query:
            print("Darvin: Good Bye sir, It was nice interacting with you, thank you")
            speak("Good Bye sir, It was nice interacting with you, thank you")
            sys.exit()

        # elif 'news' in query: 
              
        #     try:  
        #         jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\timesofIndiaApikey\\''') 
        #         data = json.load(jsonObj) 
        #         i = 1
                  
        #         speak('here are some top news from the times of india') 
        #         print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
        #         for item in data['articles']: 
                      
        #             print(str(i) + '. ' + item['title'] + '\n') 
        #             print(item['description'] + '\n') 
        #             speak(str(i) + '. ' + item['title'] + '\n') 
        #             i += 1
        #     except Exception as e: 
                  
        #         print(str(e))

        # elif 'thought of the day' in query:

        # else:
        #     speak("I can search the web for you, Do you want to continue?") 
        #     ans = takeCommand() 
        #     if 'yes' in str(ans) or 'yeah' in str(ans): 
        #         for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        #             webbrowser.open("https://google.com/search?q=%s" % query) 
            # else: 
               # return 0

        elif 'artificial intelligence' in query:
            print("Darvin: In computer science, artificial intelligence, sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans")
            speak("In computer science, artificial intelligence, sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans")

        # elif 'what is' in query:
        #     query = query.replace("what is ", "")
        #     try:
        #         results = wikipedia.summary(query, sentences=2)
        #         speak("According to Wikipedia...")
        #         print("Darvin:")
        #         Query = (float(query))
        #         results = Query
        #         print(results)
        #         speak(results)
        #         indx = input.lower().split().index('query') 
        #         Query = input.split()[indx + 1:] 
        #         res = client.Query(' '.join(Query)) 
        #         answer = next(res.results).text 
        #         assistant_speaks("The answer is " + answer) 
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Samarjeet.... I am not able to search rite now...")