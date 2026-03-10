import speech_recognition as sr


import setuptools as st
import pyaudio as pa
import webbrowser as wb
import pyttsx3 as pytt

# creating an recognizer object:

recognizer = sr.Recognizer()
# initilising text to speech module:
engine = pytt.init()


# text to speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    # Listen for the wake word "hey shenana are u up"
        # obtain audio from the microphone


if __name__ == "__main__":
    speak("for you sir,always")
    while True:

        # obtain audio from microphone
        with sr.Microphone() as source:

            print("Say something!")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_sphinx(audio)
            print("Sphinx thinks you said: " + command)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")

        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
