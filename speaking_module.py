import speech_recognition as sr

def getCommand():
    audio = sr.Recognizer()

    with sr.Microphone() as sound_source:
        print("Waitin' for a command ...")
        audio.adjust_for_ambient_noise(sound_source)
        audio.pause_threshold = 1
        voice_command = audio.listen(sound_source)

    try:
        print("Trying to recognize your mumbling ...")
        query = audio.recognize_google(voice_command, language='en-in')
        print(f'You said: {query}')
    except Exception as err:
        print(err)
        print("Unable to recognize your mumbling.")
        return 1
    
    return query

''' Testing Stuff: '''
# s = getCommand()
# print("The text was: ", s)
