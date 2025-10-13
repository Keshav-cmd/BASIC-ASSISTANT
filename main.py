import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3

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

        elif "quit" in query or "exit" in query or "sleep" in query:
            say("Goodbye! Shutting down.")
            exit()
        
        # This is the fallback for when no command is recognized
        elif query: # Only respond if the query is not empty
            say("I can do simple tasks like open websites or tell the time. Please try a different command.")