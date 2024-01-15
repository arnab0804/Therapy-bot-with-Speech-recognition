import speech_recognition as sr
import pyttsx3

recognizer=sr.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

print("Start Speaking:")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=0.1)
    audio=recognizer.listen(source)

    text=recognizer.recognize_google(audio)
    text=text.lower()

    print('Spoken Text: '+text)