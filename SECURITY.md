


# Security Policy

## Supported Versions
Only the current version of this project is supported.

## Reporting a Vulnerability

If you find a security vulnerability in this project, please do not open a public issue. Instead, please send an email directly to [YOUR_EMAIL@ADDRESS.com].

## Privacy & Data Handling

### Voice Data
This application uses the Google Speech Recognition API (`speech_recognition` library).
*   **What happens:** When you speak, your audio data is sent to Google's servers for processing.
*   **Privacy Note:** Your voice commands are processed over the internet. Do not use this assistant to speak sensitive personal information, passwords, or medical data.

### Local Files
The application creates and reads a local text file named `notes.txt`.
*   **Risk:** If this script is run on a shared computer, other users may be able to read the notes stored in this file.

## Known Security Considerations

### 1. Code Execution (Calculator)
The calculator feature uses Python's built-in `eval()` function to solve math problems.
*   **Risk:** While convenient, `eval()` can execute arbitrary code if the input is not strictly sanitized.
*   **Example:** If a malicious user inputs commands instead of math, they could potentially execute system commands.
*   **Mitigation:** For a personal assistant, this risk is acceptable for learning purposes. However, in a production environment, you should use a dedicated math parser library instead of `eval()`.

### 2. System Commands
The application uses `os.system()` to open terminals and file managers.
*   **Risk:** Ensure that you do not modify the code to accept user input directly into `os.system()` without sanitization, as this could lead to Command Injection vulnerabilities.

## Disclaimer
This project is intended for educational purposes and personal use. It is not designed, audited, or hardened for enterprise security environments.


