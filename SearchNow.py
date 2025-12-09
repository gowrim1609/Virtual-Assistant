import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said:{query}\n")
    except Exception as e:
        speak("say that again...")
        return "None"
    return query


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("panda", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("no speakable output available")


def searchYoutube(query):
    if "Youtube" in query:
        speak("this is what i found for your search")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("panda", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done ,mam")



def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("panda", "")
        results = wikipedia.summary(query,2)
        speak("according to wikipedia..")
        print(results)
        speak(results)
