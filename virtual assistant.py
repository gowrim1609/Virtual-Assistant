import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import subprocess
import wikipedia
import pyaudio
import cv2
import pyautogui

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to recognize your voice.")
            return "None"
        return query

def greetUser():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def waitForWakeWord():
    print("Say 'Panda' or 'Hey Panda' to activate...")
    while True:
        query = takeCommand().lower()
        if 'panda' in query or 'hey panda' in query:
            greetUser()
            return
def tellTime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")

def tellDate():
    date = datetime.datetime.now().date()
    speak(f"Today's date is {date}")

def openApplication(appName):
    if appName == "excel":
        subprocess.Popen(["start", "excel"], shell=True)
    elif appName == "word":
        subprocess.Popen(["start", "winword"], shell=True)
    # Add more applications as needed

def closeApplication(appName):
    try:
        if os.name == "nt":  # Windows
            subprocess.Popen(["taskkill", "/f", "/im", f"{appName}.exe"], shell=True)
            print(f"{appName} closed successfully.")
        else:
            print("Application closing is not supported on this platform.")
    except Exception as e:
        print(f"Error closing {appName}: {e}")


def searchWeb(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def searchYoutube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def get_wikipedia_summary(topic):
    try:
        # Get the summary of the topic
        summary = wikipedia.summary(topic, sentences=5)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Disambiguation error: {e.options}")
    except wikipedia.exceptions.PageError:
        speak("Page not found.")
    except Exception as e:
        speak(str(e))

def openCamera():
    camera = cv2.VideoCapture(0)
    return camera

def captureImage(camera):
    ret, image = camera.read()
    if ret:
        cv2.imwrite("captured_image.jpg", image)
        print("Image captured successfully.")
    else:
        print("Error capturing image.")

def showImage():
    image_path = "captured_image.jpg"
    if os.path.exists(image_path):
        image = cv2.imread(image_path)
        cv2.imshow("Captured Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No captured image found.")

def takeScreenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("Screenshot captured successfully.")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")

def showScreenshot():
    screenshot_path = "screenshot.png"
    if os.path.exists(screenshot_path):
        screenshot = cv2.imread(screenshot_path)
        cv2.imshow("Screenshot", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No screenshot found.")



def main():
    camera = openCamera()
    waitForWakeWord()
    speak("I am Panda, your personal assistant. How can I assist you today?")
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            tellTime()
        elif 'date' in query:
            tellDate()
        elif 'set alarm' in query:
            # Implement alarm functionality
            speak("What time should I set the alarm for?")
            alarm_time = takeCommand().lower()
            # Implement alarm functionality with alarm_time
            speak(f"Setting an alarm for {alarm_time}...")
        elif 'to do list' in query:
            # Implement to-do list functionality
            speak("What would you like to add to your to-do list?")
            todo_item = takeCommand().lower()
            # Add todo_item to the to-do list
            speak(f"I've added {todo_item} to your to-do list.")
        elif 'open' in query:
            app = query.replace('open ', '')
            openApplication(app)
        elif 'close' in query:
            app_to_close = query.replace('close ', '')
            closeApplication(app_to_close)
        elif 'search' in query:
            speak("What should I search for on Google?")
            search_query = takeCommand().lower()
            searchWeb(search_query)
        elif 'youtube' in query:
            speak("What should I search for on YouTube?")
            youtube_query = takeCommand().lower()
            searchYoutube(youtube_query)
        elif 'wikipedia' in query:
            speak('What would you like to search for on Wikipedia?')
            wiki_query = takeCommand().lower()
            get_wikipedia_summary(wiki_query)
        elif 'capture image' in query:
            captureImage(camera)
        elif 'show image' in query:
            showImage()
        elif 'take screenshot' in query:
            takeScreenshot()
        elif 'show screenshot' in query:
            showScreenshot()

        elif 'bye' in query:
            speak("Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    main()