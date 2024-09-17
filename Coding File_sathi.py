import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import subprocess
import random
listener = sr.Recognizer()
engine = pyttsx3.init()

# Define the function to speak

def talk(text, emotion=None):
    emotions = {
        "happy": ["I'm feeling happy! ", "That's great!", "I'm so excited! "],
        "sad": ["I'm feeling a bit down. ", "I'm here to cheer you up.", "I'm sorry to hear that. "],
        "confused": ["I'm not sure about that. ", "Can you please clarify?", "I need more information. "],
    }

    if emotion:
        response = random.choice(emotions.get(emotion, []))
        text = response + text
    engine.say(text)
    engine.runAndWait()

# Define the function to determine the time of day and greet accordingly
def greet():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        talk("Good morning, sir! I'm your voice assistant Chris. How can I assist you today?")
    elif datetime.time(12) <= current_time < datetime.time(17):
        talk("Good afternoon, sir! I'm your voice assistant Chris. How can I assist you today?")
    elif datetime.time(17) <= current_time < datetime.time(20):
        talk("Good evening, sir! I'm your voice assistant Chris. How can I assist you today?")
    else:
        talk("Good night, sir! I'm your voice assistant Chris. How can I assist you today?")

# Greet the user
greet()

# Define the function to take a voice command
def take_command():
    command=""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'chris' in command:
                command = command.replace('chris', '')
                print(command)
            if 'stop listening' in command:
                talk('Goodbye, sir. Have a great day!')
                exit()  # This command will exit the program
    except:
       pass
    return command

# Define the function to run the voice assistant
def run_chris():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        person = command.replace('who is', '').replace('what is', '').replace('tell me about', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open chrome' in command:
        talk('Opening Google Chrome')
        try:
            subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
        except Exception as e:
            print(f"Error opening Chrome: {e}")

    elif 'open youtube' in command:
        talk('Opening YouTube in Microsoft Edge')
        url = 'https://www.youtube.com'
        webbrowser.get('windows-default').open(url)

# Start the voice assistant
while True:
    run_chris()
