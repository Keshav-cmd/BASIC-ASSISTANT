
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import wikipedia  # New import for Wikipedia search
import platform   # New import for system info

# --- Initialize the text-to-speech engine ---
engine = pyttsx3.init()

def say(text):
    """Speaks the given text."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listens for a command and returns it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        say("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

if __name__ == '__main__':
    say("Initializing Simple Assistant. I. am. ready. SIRR")
    
    while True:
        query = takeCommand()

        # --- Task Execution using if/elif/else ---
        
        if "open youtube" in query:
            say("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            say("Opening Google.")
            webbrowser.open("https://www.google.com")
        
        elif "open github" in query:
            say("Opening GitHub.")
            webbrowser.open("https://www.github.com")

        elif "the time" in query:
            str_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The current time is {str_time}")

        elif "open terminal" in query:
            say("Opening a new terminal.")
            # This command is for Linux Mint/Ubuntu
            os.system("gnome-terminal")
        
        elif "open file manager" in query:
            say("Opening the file manager.")
            # This command is for Linux Mint/Ubuntu
            os.system("xdg-open .")

        # --- NEW FEATURES START HERE ---

        elif "search for" in query:
            # Extracts the part after "search for" and Googles it
            search_term = query.replace("search for", "")
            say(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")

        elif "wikipedia" in query:
            say("Searching Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                say("According to Wikipedia")
                print(results)
                say(results)
            except Exception as e:
                say("Sorry, I couldn't find anything on Wikipedia for that.")

        elif "the date" in query:
            str_date = datetime.datetime.now().strftime("%Y-%m-%d")
            say(f"Today's date is {str_date}")

        elif "who are you" in query or "about you" in query:
            say("I am a simple Python voice assistant running on your machine. I can help you with basic tasks.")

        elif "who made you" in query:
            say("I was created by a programmer using Python, SpeechRecognition, and pyttsx3 libraries.")

        elif "system info" in query or "my system" in query:
            say(f"You are running {platform.system()} version {platform.release()}.")
            say(f"Your processor is {platform.processor()}")

        elif "open stackoverflow" in query:
            say("Opening Stack Overflow.")
            webbrowser.open("https://www.stackoverflow.com")

        elif "open gmail" in query:
            say("Opening Gmail.")
            webbrowser.open("https://mail.google.com")

        elif "open spotify" in query:
            say("Opening Spotify.")
            webbrowser.open("https://www.spotify.com")

        elif "play music" in query:
            # Opens a generic music search or a specific playlist
            say("Opening music on YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=music")

        elif "clear screen" in query or "clear terminal" in query:
            say("Clearing the terminal screen.")
            os.system("clear") # Use 'cls' if you are on Windows

        # --- EXIT COMMANDS ---
        
        elif "quit" in query or "exit" in query or "sleep" in query:
            say("Goodbye! Shutting down.")
            exit()
        
        # This is the fallback for when no command is recognized
        elif query: # Only respond if the query is not empty
            say("I can do simple tasks like open websites, tell the time, or search Wikipedia. Please try a different command.")
