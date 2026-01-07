import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import wikipedia  # Import for Wikipedia search
import platform   # Import for system info

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

        # --- PREVIOUSLY ADDED FEATURES ---

        elif "search for" in query:
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
            say("Opening music on YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=music")

        elif "clear screen" in query or "clear terminal" in query:
            say("Clearing the terminal screen.")
            os.system("clear") # Use 'cls' if you are on Windows

        # --- NEW FEATURES START HERE ---

        elif "calculate" in query:
            # Simple math calculator
            try:
                # Extract the part after "calculate"
                expr = query.replace("calculate", "")
                print(f"Calculating: {expr}")
                # eval evaluates a string as a python expression (e.g., "5 + 3")
                result = eval(expr) 
                say(f"The result is {result}")
            except Exception:
                say("Sorry, I couldn't calculate that. Please say it like 'calculate 5 plus 3'.")

        elif "take a screenshot" in query or "screenshot" in query:
            try:
                import pyautogui
                say("Taking a screenshot in 3 seconds.")
                # Sleep to give time to switch windows if needed
                import time
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save("screenshot.png")
                say("Screenshot saved to your folder.")
            except ImportError:
                say("You need to install pyautogui to use this feature.")
            except Exception as e:
                say("Could not take screenshot.")

        elif "tell me a joke" in query or "joke" in query:
            try:
                import pyjokes
                joke = pyjokes.get_joke()
                say(joke)
            except ImportError:
                say("You need to install pyjokes to hear jokes.")
            except Exception:
                say("I couldn't think of a joke right now.")

        elif "make a note" in query or "remember this" in query:
            try:
                note = query.replace("make a note", "").replace("remember this", "")
                with open("notes.txt", "a") as f:
                    f.write(note + "\n")
                say("I have saved that note to a file.")
            except Exception:
                say("Sorry, I couldn't save the note.")

        elif "read notes" in query or "show notes" in query:
            try:
                with open("notes.txt", "r") as f:
                    content = f.read()
                if content:
                    say("Here are your notes:")
                    print(content)
                    # Reading long text can be buggy with TTS, so we print it too
                    say(content) 
                else:
                    say("You have no saved notes.")
            except FileNotFoundError:
                say("You don't have any saved notes yet.")
            except Exception:
                say("Sorry, I couldn't read the notes.")

        elif "weather" in query:
            say("Showing weather in your browser.")
            # Google weather detects location automatically
            webbrowser.open("https://www.google.com/search?q=weather")

        # --- ADDITIONAL NEW FEATURES ---

        elif "open reddit" in query:
            say("Opening Reddit.")
            webbrowser.open("https://www.reddit.com")

        elif "open twitter" in query or "open x" in query:
            say("Opening Twitter.")
            webbrowser.open("https://www.twitter.com")

        elif "open instagram" in query:
            say("Opening Instagram.")
            webbrowser.open("https://www.instagram.com")

        elif "open linkedin" in query:
            say("Opening LinkedIn.")
            webbrowser.open("https://www.linkedin.com")

        elif "open facebook" in query:
            say("Opening Facebook.")
            webbrowser.open("https://www.facebook.com")

        elif "open amazon" in query:
            say("Opening Amazon.")
            webbrowser.open("https://www.amazon.com")

        elif "open netflix" in query:
            say("Opening Netflix.")
            webbrowser.open("https://www.netflix.com")

        elif "open whatsapp" in query:
            say("Opening WhatsApp Web.")
            webbrowser.open("https://web.whatsapp.com")

        elif "open discord" in query:
            say("Opening Discord.")
            webbrowser.open("https://discord.com/app")

        elif "battery" in query or "battery status" in query:
            try:
                import psutil
                battery = psutil.sensors_battery()
                if battery:
                    percent = battery.percent
                    plugged = battery.power_plugged
                    status = "plugged in" if plugged else "not plugged in"
                    say(f"Battery is at {percent} percent and {status}")
                else:
                    say("Could not detect battery information.")
            except ImportError:
                say("You need to install psutil to check battery status.")
            except Exception:
                say("Could not retrieve battery information.")

        elif "cpu usage" in query or "cpu" in query:
            try:
                import psutil
                cpu_percent = psutil.cpu_percent(interval=1)
                say(f"CPU usage is at {cpu_percent} percent")
            except ImportError:
                say("You need to install psutil to check CPU usage.")
            except Exception:
                say("Could not retrieve CPU information.")

        elif "memory usage" in query or "ram usage" in query:
            try:
                import psutil
                memory = psutil.virtual_memory()
                say(f"Memory usage is at {memory.percent} percent")
            except ImportError:
                say("You need to install psutil to check memory usage.")
            except Exception:
                say("Could not retrieve memory information.")

        elif "set alarm" in query or "alarm" in query:
            try:
                import time
                say("For how many seconds from now?")
                alarm_time = takeCommand()
                seconds = int(''.join(filter(str.isdigit, alarm_time)))
                say(f"Setting alarm for {seconds} seconds from now.")
                time.sleep(seconds)
                say("Wake up! Your alarm is ringing!")
                for i in range(3):
                    print("\a")  # System beep
            except Exception:
                say("Sorry, I couldn't set the alarm.")

        elif "set timer" in query or "timer" in query:
            try:
                import time
                say("For how many seconds?")
                timer_input = takeCommand()
                seconds = int(''.join(filter(str.isdigit, timer_input)))
                say(f"Timer set for {seconds} seconds.")
                time.sleep(seconds)
                say("Time's up!")
                for i in range(3):
                    print("\a")
            except Exception:
                say("Sorry, I couldn't set the timer.")

        elif "flip a coin" in query or "coin flip" in query:
            import random
            result = random.choice(["Heads", "Tails"])
            say(f"The coin landed on {result}")

        elif "roll a dice" in query or "roll dice" in query:
            import random
            result = random.randint(1, 6)
            say(f"You rolled a {result}")

        elif "random number" in query:
            import random
            number = random.randint(1, 100)
            say(f"Your random number is {number}")

        elif "ip address" in query or "my ip" in query:
            try:
                import socket
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                say(f"Your local IP address is {ip_address}")
            except Exception:
                say("Could not retrieve IP address.")

        elif "search youtube for" in query:
            search_term = query.replace("search youtube for", "")
            say(f"Searching YouTube for {search_term}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")

        elif "news" in query:
            say("Opening Google News.")
            webbrowser.open("https://news.google.com")

        elif "maps" in query or "open maps" in query:
            say("Opening Google Maps.")
            webbrowser.open("https://www.google.com/maps")

        elif "translate" in query:
            say("Opening Google Translate.")
            webbrowser.open("https://translate.google.com")

        elif "delete notes" in query or "clear notes" in query:
            try:
                with open("notes.txt", "w") as f:
                    f.write("")
                say("All notes have been deleted.")
            except Exception:
                say("Could not delete notes.")

        elif "shutdown" in query or "shutdown system" in query:
            say("Shutting down the system in 10 seconds. Say cancel to stop.")
            import time
            time.sleep(5)
            # Uncomment the line below to actually shutdown (use with caution!)
            # os.system("shutdown now")  # Linux
            # os.system("shutdown /s /t 1")  # Windows
            say("Shutdown cancelled for safety. Uncomment code to enable.")

        elif "restart" in query or "restart system" in query:
            say("Restarting the system in 10 seconds. Say cancel to stop.")
            import time
            time.sleep(5)
            # Uncomment the line below to actually restart (use with caution!)
            # os.system("reboot")  # Linux
            # os.system("shutdown /r /t 1")  # Windows
            say("Restart cancelled for safety. Uncomment code to enable.")

        elif "lock screen" in query or "lock system" in query:
            say("Locking the screen.")
            # os.system("gnome-screensaver-command -l")  # Linux Mint/Ubuntu
            # os.system("rundll32.exe user32.dll,LockWorkStation")  # Windows
            say("Lock command is commented out for safety. Uncomment to enable.")

        elif "create folder" in query or "new folder" in query:
            try:
                say("What should I name the folder?")
                folder_name = takeCommand()
                os.makedirs(folder_name, exist_ok=True)
                say(f"Folder {folder_name} created successfully.")
            except Exception:
                say("Could not create folder.")

        elif "list files" in query or "show files" in query:
            try:
                files = os.listdir(".")
                say(f"You have {len(files)} files and folders here.")
                print(files)
            except Exception:
                say("Could not list files.")

        elif "volume up" in query or "increase volume" in query:
            say("Increasing volume.")
            # os.system("amixer -D pulse sset Master 10%+")  # Linux
            # For Windows, you'd need a different approach
            say("Volume control is system-specific. Uncomment appropriate command.")

        elif "volume down" in query or "decrease volume" in query:
            say("Decreasing volume.")
            # os.system("amixer -D pulse sset Master 10%-")  # Linux
            say("Volume control is system-specific. Uncomment appropriate command.")

        elif "mute" in query:
            say("Muting volume.")
            # os.system("amixer -D pulse sset Master mute")  # Linux
            say("Mute control is system-specific. Uncomment appropriate command.")

        elif "unmute" in query:
            say("Unmuting volume.")
            # os.system("amixer -D pulse sset Master unmute")  # Linux
            say("Unmute control is system-specific. Uncomment appropriate command.")

        elif "day of week" in query or "what day" in query:
            day = datetime.datetime.now().strftime("%A")
            say(f"Today is {day}")

        elif "month" in query or "what month" in query:
            month = datetime.datetime.now().strftime("%B")
            say(f"The current month is {month}")

        elif "year" in query or "what year" in query:
            year = datetime.datetime.now().strftime("%Y")
            say(f"The current year is {year}")

        elif "motivate me" in query or "motivation" in query:
            import random
            quotes = [
                "Believe you can and you're halfway there.",
                "The only way to do great work is to love what you do.",
                "Don't watch the clock; do what it does. Keep going.",
                "The future belongs to those who believe in the beauty of their dreams.",
                "Success is not final, failure is not fatal: It is the courage to continue that counts."
            ]
            say(random.choice(quotes))

        elif "speed test" in query or "internet speed" in query:
            say("Opening speed test in browser.")
            webbrowser.open("https://fast.com")

        elif "help" in query or "what can you do" in query:
            say("I can open websites, tell time and date, search Wikipedia, take notes, tell jokes, calculate math, take screenshots, check system info, battery, CPU, memory, set timers, flip coins, and much more. Just ask!")

        # --- EXIT COMMANDS ---
        
        elif "quit" in query or "exit" in query or "sleep" in query:
            say("Goodbye! Shutting down.")
            exit()
        
        # This is the fallback for when no command is recognized
        elif query: 
            say("I can do simple tasks like open websites, tell the time, take notes, or search Wikipedia. Please try a different command.")
