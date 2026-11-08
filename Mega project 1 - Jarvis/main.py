import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key = "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")

    response = client.responses.create(
    model="gpt-6-astra",
    input=command,
    )

    return response.output_text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
            #parse the json response
            data = r.json()

            #extract the articles
            articles = data.get('articles',[])

            # speak the headlines
            for article in articles:
                speak(article['title'])

    else:
        #Let openAI handle the request
        answer = aiProcess(c)
        print(answer)







    
    
if __name__ =="__main__":
    speak("Initializing Jarvis ......")
    
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio for microphone
        r = sr.Recognizer()
        

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening .....")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("yeah")
                # Listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("error; {0}".format(e))