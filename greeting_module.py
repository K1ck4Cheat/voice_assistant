import pyttsx3
import datetime
import file_actions as fa
import speaking_module as sm


# Setting TextToSpeach engine for Windows
engine = pyttsx3.init('sapi5')
# Setting the engine voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Setting the voice volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)
# Setting the voice rate (speech speed)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# Saving the settings to a file
fa.save_setting('engine', 'sapi5')
fa.save_setting('voice', '1')
fa.save_setting('volume', '1')
fa.save_setting('rate', '150')


# Assistant name:
assistant_name = 'Friday'
file_name = fa.file_name

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def say_my_name():
    if not fa.check_in_file(file_name, 'name'):
        speak("I don't know your name, Sir!")
        speak("Please say loudly your name to register you in my database")
        name = sm.getCommand()
        print("Your name is ", name, "?")
        f = open(file_name, 'a')
        f.write(f'name:{name}\n') 
        f.close()
    else:
        f = open(file_name, 'r')
        name = fa.get_setting(file_name, 'name')
    return name


def greeting():
    name = say_my_name()
    hour = int(datetime.datetime.now().hour)
    if 2 <= hour <= 11:
        speak(f"Good Morning, {name}!")
    elif 12 <= hour <= 18:
        speak(f"Good Afternoon, {name}!")
    else:
        speak(f"Good Evening, {name}!")
