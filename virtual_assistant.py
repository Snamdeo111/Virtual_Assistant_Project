import speech_recognition as sr
import pyttsx3
import sys
import location as loc
import webbrowser
from forecastiopy import ForecastIO,FIOHourly
import applist as app_list
import wikipedia
from wikipedia import exceptions
import datetime
import file_path_find as fd
import os
import urllib.request
import urllib.parse
import random
import re
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[1].id)

def mavis_response(audio):
    engine.say(audio)
    engine.runAndWait()

def mycommand():
    x=str(input("Query : "))
    return x

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
        mavis_response('you said'+query)
        mavis_response('okay')
    except Exception as e:
        return "None"

    return query

def assistant(command):
        if 'shutdown' in command:
            mavis_response('Bye bye Sir. Have a nice day')
            sys.exit()
        elif 'close' in command:
            Exe=command.split('close')
            Exe=Exe[1]+'.exe'
            os.system("taskkill /f /im " + Exe)
        elif 'launch' in command:
            name = command.split('launch ')
            mavis_response('launching'+name[1])
            name = name[1]+'.exe'
            file_path = fd.file_equal_search(name)
            os.startfile(file_path)
        elif 'Wikipedia' in command:
            query = command.split("for ")
            query = query[1]
            try:

                mavis_response('Searching Wikipedia for ' + query)
                results = wikipedia.summary(query, sentences=2)
                print(results, sep='.')
                mavis_response("According to Wikipedia")
                mavis_response(results)
            except exceptions.DisambiguationError as error:
                mavis_response("Disambiguition while searching for "+query)
                mavis_response(query+' may refer to one of the following ')
                for i in range(len(error.options)):
                    print(error.options[i])
                    mavis_response(error.options[i])
                pass
        elif 'list programs' in command:
            mavis_response('Wait. Scanning your device')
            app_list.list()
            mavis_response('These are all the installed programs')

        elif 'search for' in command:
            search = command.split('for ')
            search = search[1]
            url = 'https://www.google.com/search?q='+search
            results = wikipedia.summary(search, sentences=2)
            webbrowser.open(url)
            mavis_response("results are opened in the browser")
            mavis_response("According to Wikipedia " + results)
        elif 'play music' in command:
            music_dir = 'C:/Users/Sachin Namdeo/Desktop/music'
            songs = os.listdir(music_dir)
            num=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir, songs[num]))
        elif 'play' in command:
            search = command.split('play ')
            search=search[1]
            query_string = urllib.parse.urlencode({"search_query": search})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
        elif 'open' in command and 'file' in command:
            if 'Word' in command:
                name = command.split('open Word file ')
                name = name[1]+'.docx'
                path = fd.file_search(name)
                os.startfile(path)
            elif 'PPT' in command:
                name = command.split('open PPT file ')
                name = name[1]+'.pptx'
                path = fd.file_search(name)
                os.startfile(path)
            elif 'PDF' in command:
                name = command.split('open PDF file ')
                name = name[1]+'.pdf'
                path = fd.file_search(name)
                os.startfile(path)
            elif 'Rar' in command:
                name = command.split('open Rar file ')
                name = name[1]+'.rar'
                path = fd.file_search(name)
                os.startfile(path)

        elif 'open website' in command:
            site = command.split('open website ')
            site = site[1]
            url = 'https://www.' + site
            webbrowser.open(url)
            mavis_response('opening '+site)

        elif 'current weather' in command:
            location = loc.locate()
            apikey=''
            lat = location[0]
            lng = location[1]
            response = ForecastIO.ForecastIO(apikey, units=ForecastIO.ForecastIO.UNITS_SI, lang=ForecastIO.ForecastIO.LANG_ENGLISH, latitude=lat, longitude=lng)
            currently = FIOHourly.FIOHourly(response)
            print(loc.place()+' has '+currently.get()['summary'])
            mavis_response(loc.place()+' has '+currently.get()['summary'])

        elif 'time' in command:
            now = datetime.datetime.now()
            mavis_response('Current time is %d hours %d minutes' % (now.hour, now.minute))


mavis_response('Hello, How Can I help you')


while True:
    assistant(myCommand())
