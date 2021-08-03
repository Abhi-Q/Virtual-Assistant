import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes
from os import system
mycooltitle = "Blaze Assistant"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

system("title "+mycooltitle)

listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'blaze' in command:
                command = command.replace('blaze', '')
                print(yellow + command)
    except:
        pass
    return command


def run_blaze():
    command = take_command()
    print(white + command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(cyan + 'Current time is ' + time)
    elif 'what is' in command:
        web = command.replace('what is', '')
        talk('Doing a web search on' + web)
        print(cyan + 'Doing a web search on' + web)
        pywhatkit.search(web)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i am in love with silcone valley')
    elif 'are you single' in command:
        talk('No not for you.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
	
    else:
        talk('Sorry! I coudnt get you. Would you be a dear and repeat that.')


while True:
    run_blaze()
