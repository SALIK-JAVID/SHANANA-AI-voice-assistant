import speech_recognition as sr


import setuptools as st
import pyaudio as pa
import webbrowser as wb
import pyttsx3 as pytt
import time

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

def processcommand(c):
    pass

if __name__ == "__main__":
    speak("Hello i'm shanana , your virtual A I assistant")
    while True:
        # Listen for the wake word "hey shenana are u up"
        # obtain audio from the microphone

        # obtain audio from microphone

        try:
            # listen the waking word
            with sr.Microphone() as source:
                print("Say something!")
                audio = recognizer.listen(source, timeout=5)
                # listen takes three inputs:()
            word = recognizer.recognize_google(audio).lower() #replacing command with word
            
            print("Shanana thinks you said: " + word) #for clarity
            if "hello" or "hey shanana" or "shanana" in word:
                speak("for you sir, always")
                time.sleep(3)
                # listening to the command:
                with sr.Microphone() as source:
                    print("shanana active")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    print("Command received:", command)
                    
                    processcommand(command)
                    
                
                
            
            # elif "youtube" in command:
            #     speak("opening youtube")
            #     time.sleep(2)
            #     wb.open("https://www.youtube.com/")
            # elif "google" in command:
            #     speak("opening google")
            #     time.sleep(2)  #
            #     wb.open("https://www.google.com/")
            # elif "shutdown" in command:
            #     print("Shutdown command detected")
            #     speak("shutting down , goodbye")
            #     time.sleep(2)
            #     exit()

        except sr.UnknownValueError:
            print("Shanana could not understand audio")

        except sr.RequestError as e:
            print("Shanana error; {0}".format(e))
