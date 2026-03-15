import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pytt
import time
import requests

# News API key
api_key = "329da15a5c9e4acba2c5f74bf8514bcb"
url = f"https://newsapi.org/v2/everything?q=ai&apiKey={api_key}"

# recognizer 
recognizer = sr.Recognizer()


# speech function (reinitializes engine every time to avoid macOS freeze)
def speak(text):
    print("Shanana:", text)
    engine = pytt.init(driverName="nsss")
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":

    speak("Hello I'm Shanana, your virtual A I assistant , say shanana to wake me up")

    while True:
        try:
            # Wake word listening
            with sr.Microphone() as source:
                print("Say something!")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio).lower()
            print("Shanana thinks you said:", word)

            if "hello" in word or "hey shanana" in word or "shanana" in word or "are u up " in word or "wake up" in word:

                speak("Hey Salik, how is your day going ")

                # Command listening
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

                # YOUTUBE
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
                elif "shutdown" in command:
                    speak("Shutting down, goodbye sir")
                    exit()
                # let open ai handle the request


        except sr.UnknownValueError:
            print("Shanana could not understand audio")

        except sr.RequestError as e:
            print("Shanana error:", e)