# Remote Encrypted Keylogger

## Overview

This repository contains a Python-based keylogger I designed to securely log keystrokes with encryption. The keylogger is suitable for controlled environments where monitoring user input is necessary. It ensures that logged data remains secure through encryption, even if the log files are compromised.


## Code Explanation:

The Enhanced Keylogger script in this repository is designed to capture keystrokes, encrypt them, and write them to a log file. This section provides a explanation of how the code works.

### 1. **Imports and Setup**

The script begins by importing necessary modules, including `pynput` for capturing keyboard events, `datetime` for timestamping, `os` and `platform` for interacting with the operating system, `threading` for handling background tasks, and `cryptography.fernet` for encryption.

### 2. **Global Variables**

- **keys**: This list temporarily stores captured keystrokes before they are written to the log file.
- **key_count**: A counter that tracks the number of keystrokes before writing to the log file.
- **log_file_path**: The path to the file where the encrypted logs will be stored.

### 3. **Encryption Key Management**

The script uses the `Fernet` encryption method to securely store logged keystrokes. It first checks if an encryption key already exists in the `key.key` file. If not, it generates a new key and stores it. This key is essential for both encrypting and decrypting the log file.

### 4. **Keystroke Logging**

The `on_press` function is triggered whenever a key is pressed. It appends the pressed key to the `keys` list, handling both regular characters and special keys (like space and enter) appropriately. After a certain number of keystrokes, the function writes the logs to the file by calling `write_file`.

### 5. **Writing Logs to a File**

The `write_file` function encrypts the collected keystrokes and writes them to the log file. The data is first timestamped, then encrypted using the previously loaded encryption key, and finally appended to the log file. After writing, the `keys` list is cleared.

### 6. **Logging System Information**

At the start of the session, the script logs basic system information, such as the operating system, node name, platform, and processor type. This information is also encrypted and stored in the log file, providing context for the captured keystrokes.

### 7. **Background Writing Process**

The `periodic_write` function ensures that the logs are regularly written to the file, even if fewer than the predefined number of keystrokes have been captured. This helps prevent data loss in case the script is interrupted. The function uses threading to periodically trigger the writing process.

### 8. **Starting the Keylogger**

The script logs system information, starts the periodic writing process, and then begins listening for keyboard events. The keylogger continues running, capturing and logging keystrokes until it is manually stopped.

## Possible Enhancements

While the keylogger is fully functional, it can be enhanced with the following features which i have implented in the python file, RemoteEnhancedlogger.py:

1. **Stealth Mode**: Run the script as a background process or a service to avoid detection, making it less visible to users.
2. **Remote Logging**: Send logs to a remote server or cloud storage, enabling remote monitoring and ensuring logs are not lost if the local machine is compromised.

## Implementing Stealth Mode and Remote Logging

### Stealth Mode

To make the keylogger run stealthily, especially on Windows, you can use `pythonw.exe` instead of `python.exe`, which suppresses the console window. Additionally, you can programmatically hide the console window using system calls.

### Remote Logging

You can set up a remote server to receive logs via HTTP POST requests. This allows for secure, remote storage of logs, enabling monitoring from different locations and ensuring logs are not lost even if the local machine is compromised.
Server Setup:
-Deploy the Flask app on a server (e.g., AWS, Heroku, DigitalOcean).
-Ensure the server is accessible and has an endpoint to handle file uploads.

**Disclaimer**: This keylogger is provided for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always ensure you have proper authorization before deploying such tools.

### DEMO:

![Alt text](https://github.com/Rafael-Nawaz/Remote-Encrypted-Keylogger-/blob/main/Screenshot%202024-08-21%20181746.png)

![Alt text](https://github.com/Rafael-Nawaz/Remote-Encrypted-Keylogger-/blob/main/Screenshot%202024-08-21%20181835.png)

![Alt text](https://github.com/Rafael-Nawaz/Remote-Encrypted-Keylogger-/blob/main/Screenshot%202024-08-21%20181920.png)

![Alt text](https://github.com/Rafael-Nawaz/Remote-Encrypted-Keylogger-/blob/main/Screenshot%202024-08-21%20181932.png)



