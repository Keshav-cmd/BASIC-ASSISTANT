


# Basic Python Voice Assistant

A desktop virtual assistant built using Python. It can understand your voice commands, perform tasks like opening websites, searching the internet, taking screenshots, managing notes, and telling the time.

## Features

- **Voice Interaction:** Uses Speech Recognition to listen and pyttsx3 to speak back to you.
- **Web Browsing:** Quickly open popular websites like YouTube, Google, GitHub, StackOverflow, Gmail, and Spotify.
- **Search Capabilities:**
  - Google Search ("Search for Python tutorials")
  - Wikipedia Summary ("Wikipedia Albert Einstein")
- **System Utilities:**
  - Tell the current Time and Date.
  - Open Terminal and File Manager (Linux/Mac).
  - Clear the terminal screen.
  - Get System Information (OS version, Processor).
- **Productivity:**
  - **Calculator:** Perform basic math ("Calculate 5 plus 3").
  - **Note Taker:** Save voice notes to a text file and read them back later.
  - **Screenshots:** Take a screenshot instantly.
- **Fun:** Tells programmer jokes.
- **Weather:** Opens the weather forecast for your location.

## Prerequisites

1.  **Python 3.x** installed on your machine.
2.  A working **Microphone**.
3.  **Internet Connection** (for voice recognition and web searches).

## Installation

You will need to install the required Python libraries. Open your terminal or command prompt and run:

```bash
pip install speechrecognition pyttsx3 wikipedia pyautogui pyjokes
```

### Note for Linux Users
If you are on Linux (Ubuntu/Mint), `SpeechRecognition` requires `PyAudio`. If the above command fails, run:
```bash
sudo apt-get install python3-pyaudio
```

### Note for Windows Users
If `pip install pyaudio` fails, you may need to download a `.whl` file or try:
```bash
pip install pipwin
pipwin install pyaudio
```

## How to Run

1.  Save the Python code as `assistant.py`.
2.  Run the script:
    ```bash
    python assistant.py
    ```
3.  The assistant will say *"Initializing Simple Assistant. I am ready. SIRR"*.
4.  Speak a command from the list below.

## Voice Commands

Here is a list of commands you can use:

| Command | Action |
| :--- | :--- |
| **"Open YouTube"** | Opens youtube.com |
| **"Open Google"** | Opens google.com |
| **"Open GitHub"** | Opens github.com |
| **"Open StackOverflow"** | Opens stackoverflow.com |
| **"Open Gmail"** | Opens Gmail |
| **"Open Spotify"** | Opens Spotify |
| **"Play Music"** | Opens a YouTube music search |
| **"Search for [query]"** | Searches Google for your query |
| **"Wikipedia [topic]"** | Reads a 2-sentence summary from Wikipedia |
| **"The time"** | Tells the current time |
| **"The date"** | Tells today's date |
| **"Calculate [math]"** | Solves math problems (e.g., "Calculate 10 times 5") |
| **"Take a screenshot"** | Takes a screenshot and saves it |
| **"Make a note [text]"** | Saves text to `notes.txt` |
| **"Read notes"** | Reads out saved notes from `notes.txt` |
| **"Tell me a joke"** | Tells a random programming joke |
| **"System info"** | Reads OS and Processor details |
| **"Weather"** | Opens Google Weather in browser |
| **"Clear screen"** | Clears the terminal output |
| **"Quit" / "Exit" / "Sleep"** | Closes the assistant |

## Troubleshooting

*   **Microphone Error:** Ensure your microphone is not being used by another application (like Zoom or Discord) when you run the script.
*   **Unknown Value Error:** Speak clearly and reduce background noise. If the assistant says "Sorry, I didn't catch that," try repeating the command.
*   **Module Not Found:** Ensure you ran all the `pip install` commands listed in the Installation section.



**Built with Python and ❤️**
```
