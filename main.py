import speech_recognition as sr


import setuptools as st
import pyaudio as pa
import webbrowser as wb
import pyttsx3 as pytt
import time
import requests 
# news api key :
api_key  = "329da15a5c9e4acba2c5f74bf8514bcb"
url = f"https://newsapi.org/v2/everything?q=ai&apiKey={api_key}"
# creating an recognizer object:

recognizer = sr.Recognizer()
# initilising text to speech module:
engine = pytt.init(driverName='nsss') #mac os needs this driver
engine.setProperty("rate", 170)
engine.setProperty("volume", 1) 



# text to speak function
def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()
    # Listen for the wake word "hey shenana are u up"
    # obtain audio from the microphone

def processcommand(c):

    # if "youtube" in c:
    #     speak("opening youtube")
    #     time.sleep(2)
    #     wb.open("https://www.youtube.com/")
    # elif "google" in c:
    #     speak("opening google")
    #     time.sleep(2)  
    #     wb.open("https://www.google.com/")
    # elif "shutdown" in c:
    #     print("Shutdown command detected")
    #     speak("shutting down , goodbye")
    #     time.sleep(2)
    #     exit()
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
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
                # listen takes three inputs:()
            word = recognizer.recognize_google(audio).lower() #replacing command with word
            
            print("Shanana thinks you said: " + word) #for clarity
            if "hello" in word or "hey shanana" in word or "shanana" in word:

                speak("hey salik how is your day going")
                time.sleep(3)
                # listening to the command:
                with sr.Microphone() as source:
                    print("shanana active")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    print("Command received:", command)
                    if "news" in command:
                        response = requests.get(url)
                        data = response.json()
                        articles = data["articles"]
                        speak("Here are the latest news headlines")
                        for article in articles[:5]:
                            print(article["title"])
                            speak(article["title"])
                            time.sleep(1.5)

                    
                    

                    
                    
                        





    
                    elif "youtube" in command:
                        # speak is not working.
                        speak("opening youtube")
                        time.sleep(3)
                        wb.open("https://www.youtube.com/")
                    elif "google" in command:
                        speak("opening google")
                        time.sleep(3)
                        wb.open("https://www.google.com/")
                    elif "shutdown" in command:
                        print("Shutdown command detected")
                        speak("shutting down , goodbye")
                        time.sleep(3)
                        exit()
    
    


    

    
      
    

    
    
    
   
                    
                    
                    
                    
                
                
            
            

        except sr.UnknownValueError:
            print("Shanana could not understand audio")

        except sr.RequestError as e:
            print("Shanana error; {0}".format(e))
