import pyaudio
import pyttsx3
import speech_recognition
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",180)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,5,8)
    try:
        print("understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said:{query}")
    except Exception as e:
        speak("say that again please.......")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query =takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe

            greetMe()

            while True:
                query=takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir ,you can call anytime")
                    break
                elif "hello" in query:
                    speak("hello sir,how are you")
                elif "i am  fine" in query:
                    speak("that's great ,sir")
                elif "how are you" in query:
                    speak("perfect ,sir")
                elif "thank you" in query:
                    speak("you are welcome,sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube " in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)




















