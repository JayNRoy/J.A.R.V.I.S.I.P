### ---- Modules Importing ---- ###
import speech_recognition as sr
import pyttsx3 as tts
import sys
import time
import random
import openai
from datetime import datetime
from additionalFunc import writeTodo, readTodo

def logConvo(action, sender="JARVISIP"):
    """A procedure to log everything that happens in conversation with the machine."""
    logger = open("logFile.log","a")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Reports the timestamp of the logged action (as a string).
    statement = timestamp + f"-> {sender}: " + str(action) + "\n"
    logger.write(statement)
    logger.close()
    print(action)
    # TODO SEND ACTION TO GUI!

# TODO MACHINE SHUTDOWN
def shutDown():
    pass

startup = [False, False, False, False]
logConvo("---- MACHINE ONLINE ----")

def sayThis(message):
    # Condenses two lines of code into one. When JARVISIP speaks to the user
    speaker.say(message)
    speaker.runAndWait()
    logConvo(message)

# Setup speaking
try:
    speaker = tts.init()
    sayThis("JARVISIP online!")
    speaker.setProperty('rate', 150)
    sayThis("Speaking capabilities online.")
    startup[0] = True
    time.sleep(0.2)
except:
    logConvo("JARVISIP failed to launch. Speaking capabilities offline.")
    logConvo("---- MACHINE OFFLINE ----")
    sys.exit("JARVISIP failed to launch. Speaking capabilities offline.")
    
# Setup listening
try:
    recogniser = sr.Recognizer()
    sayThis("Listening capabilities online.")
    startup[1] = True
except:
    sayThis("Warning! Listening capabilities offline.")
time.sleep(0.2)
    
# Setup OpenAI GPT
try:
    sayThis("GPT machine online.")
    startup[2] = True
except:
    sayThis("Warning! GPT machine offline.")
time.sleep(0.2)
 
# Setup admin functions
try:
    sayThis("Admin functionality online.")
    startup[3] = True
except:
    sayThis("Warning! Admin functionality offline.")
time.sleep(0.2)  

# When the user responds to the assistant
def detectResponse(name="User"):
    """A function that carefully listens to a user's input response to the assistant's message."""
    global recogniser
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                # Adjust for ambient noise and listen
                recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recogniser.listen(mic)
                
                # Translate audio input to words.
                inputData = recogniser.recognize_google(audio)
                inputData = inputData.lower()
                logConvo(f"{inputData}", name)
                return inputData
        except sr.UnknownValueError:
            # In case there is an error in listening for a response.
            recogniser = sr.Recognizer
            sayThis("Sorry, I did not understand that response! Please try again.")

"""
MAIN LOOP:
JARVISIP greets user, and reports being online.
It then asks the user for a prompt.
If the prompt is specific to JARVISIP, look at intents file and respond.
Otherwise it is a normal prompt, JARVISIP feeds it to GPT3.5 / GPT4.
It then translates the response to the prompt to audio.
It then repeats until the user leaves.
While all of this happens a text version of the conversation is logged.
"""
# Launch GUI for green-light and settings menu.
responses = ["I am JARVISIP but you can call me Jarv!", "My name is JARVISIP!", "Welcome back!"]
num = random.randint(0,3)
sayThis("Hello! " + responses[num])

if False in startup:
    greet = "JARVISIP is partially operational."
else:
    greet = "JARVISIP is fully operational."
sayThis(greet)
time.sleep(0.2)

sayThis("Please tell me your name.")
UserName = detectResponse()

num = random.randint(0,2)
if num == 0:
    ask = "How can I help you today?"
else:
    ask = "What can I do for you?"
sayThis(f"Nice to meet you, {UserName}! {ask}")

userOnline = True
while userOnline == True:
    if userOnline == False:
        shutDown()
        break
    query = detectResponse(UserName)
    # Check intents file functionality
    # Else use OpenAI GPT machine
    response = "TODO"
    sayThis("TODO")

# TODO FUTURE FEATURE
# Data setup (context of the user)
todo = readTodo()