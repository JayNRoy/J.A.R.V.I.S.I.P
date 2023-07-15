### ---- Modules Importing ---- ###
import speech_recognition as sr
import pyttsx3 as tts
import sys
import openai
from additionalFunc import writeTodo, readTodo

# Setup speaking and listening
recogniser = sr.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

""" FUTURE FEATURE
# Data setup (context of the user)
todo = readTodo()
"""