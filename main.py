import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pytt
import time
import requests

# adding api to .env
from dotenv import load_dotenv
import os
load_dotenv()
# importing groq api
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# News API key
api_key =  os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=ai&apiKey={api_key}"

# recognizer 
recognizer = sr.Recognizer()


# speech function
def speak(text):
    print("Shanana:", text)
    engine = pytt.init(driverName="nsss")
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1)
    engine.say(text)
    engine.runAndWait()


# adding groq function in the code for general questions:
def ask_ai(question):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Shanana, a helpful AI voice assistant like Seri and Alexa, Always reply in 1-2 short sentences only"},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    return answer
active = False

if __name__ == "__main__":

    speak("Hello I'm Shanana, your virtual A I assistant..... say shanana to wake me up")

    while True:
        try: 

            # slep mode
            if not active:
                with sr.Microphone() as source:
                    print("Say something!")  
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)

                word = recognizer.recognize_google(audio).lower()
                print("Shanana thinks you said:", word)

                if "hello" in word or "hey shanana" in word or "shanana" in word or "are u up" in word or "wake up" in word:

                    speak("wel come back sir...")
                    time.sleep(1.1)
                    speak("congratulations our system is fully operational")

                    active = True


            # active mode 
            else:

                with sr.Microphone() as source:
                    print("Shanana active")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio).lower()
                print("Command received:", command)


                # NEWS ai
                if "news" in command:

                    response = requests.get(url)
                    data = response.json()
                    articles = data["articles"]

                    speak("Here are the latest news headlines")

                    for article in articles[:5]:
                        title = article["title"]
                        print(title)
                        speak(title)
                        time.sleep(1.8)


                # YOUTUBE.?
                elif "youtube" in command:
                    speak("Opening YouTube")
                    time.sleep(1)
                    wb.open("https://www.youtube.com")


                # GOOGLE
                elif "google" in command:
                    speak("Opening Google")
                    time.sleep(1)
                    wb.open("https://www.google.com")


                # SHUTDOWN
                elif "shut down" in command:
                    speak("Shutting down, goodbye sir")
                    exit()


                # SLEEP MODE COMMAND
                elif "sleep" in command or "shut down" in command or "mute" in command:
                    speak("Going back to sleep sir")
                    active = False
                # general questions
                else:
                    answer = ask_ai(command)
                    speak(answer)


        except sr.UnknownValueError:
            print("Shanana could not understand audio")

        except sr.RequestError as e:
            print("Shanana error:", e)
