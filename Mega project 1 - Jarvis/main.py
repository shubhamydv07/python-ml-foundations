import os
import webbrowser
import requests
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
import musicLibrary
from client import ask_ai

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init()  # fresh engine each time avoids the silent-after-first-call bug
    engine.say(text)
    engine.runAndWait()
    engine.stop()


SITES = {
    "google": "https://google.com",
    "youtube": "https://www.youtube.com",
    "linkedin": "https://www.linkedin.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://facebook.com",
    "chat gpt": "https://chatgpt.com",
}


def get_news(limit=5):
    try:
        r = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={"country": "in", "pageSize": limit},
            headers={"X-Api-Key": NEWS_API_KEY},
            timeout=8,
        )
        data = r.json()
        if r.status_code != 200:
            print("News error:", data.get("message"))
            speak("I couldn't fetch the news.")
            return
        articles = data.get("articles", [])
        if not articles:
            speak("No headlines found.")
            return
        speak("Here are the top headlines.")
        for a in articles:
            speak(a["title"])
    except Exception as e:
        print("News exception:", e)
        speak("News request failed.")


def processCommand(command):
    c = command.lower().strip()
    print("Command:", c)

    for name, url in SITES.items():
        if f"open {name}" in c:
            webbrowser.open(url)
            return

    if c.startswith("play "):
        song = c[5:].strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"I don't have {song} in my library.")
    elif "news" in c.split():
        get_news()
    else:
        speak(ask_ai(command))  # everything else goes to Gemini


def listen_once(r, source, timeout, limit):
    """Returns recognized text, or None if nothing usable was heard."""
    try:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=limit)
        return r.recognize_google(audio)
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return None
    except Exception as e:
        print("Recognition error:", e)
        return None


if __name__ == "__main__":
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:  # one mic session for the whole run
        print("Calibrating for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        speak("Jarvis online.")

        while True:
            text = listen_once(r, source, timeout=5, limit=4)
            if not text:
                continue
            print("Heard:", text)

            if "jarvis" in text.lower():
                # supports "Jarvis what is a mutex" in one breath
                command = text.lower().split("jarvis", 1)[1].strip()
                if not command:
                    speak("Yes?")
                    command = listen_once(r, source, timeout=6, limit=10)
                    if not command:
                        speak("I didn't catch that.")
                        continue
                processCommand(command)