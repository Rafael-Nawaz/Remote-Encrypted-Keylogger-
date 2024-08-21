Remote Encrypted Keylogger: Technical Write-Up
Overview
This repository contains a Python-based keylogger that logs keystrokes, encrypts the data, and provides various features to enhance functionality and security. The keylogger is designed to run on systems where logging user input is necessary, such as for monitoring in a controlled environment. The logs are encrypted using a symmetric key to ensure that even if the log files are compromised, the data remains secure.

Key Features
Keystroke Logging: Captures every keystroke on the system.
Encryption: Utilizes symmetric encryption (Fernet) to securely store logged keystrokes.
Timestamping: Logs are timestamped to provide context for each keystroke.
Background Writing: Periodically writes logs to a file and clears the memory buffer to avoid data loss.
System Information Logging: Logs basic system information at the start of the session.
Extensibility: Can be enhanced with additional features such as stealth mode and remote logging.
