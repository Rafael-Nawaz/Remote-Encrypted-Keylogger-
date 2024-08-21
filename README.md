# Remote Encrypted Keylogger

## Overview

This repository contains a Python-based keylogger designed to securely log keystrokes with encryption. The keylogger is suitable for controlled environments where monitoring user input is necessary. It ensures that logged data remains secure through encryption, even if the log files are compromised.

## Key Features

- **Keystroke Logging**: Captures every keystroke on the system.
- **Encryption**: Utilizes symmetric encryption (Fernet) to securely store logged keystrokes.
- **Timestamping**: Logs are timestamped to provide context for each keystroke.
- **Background Writing**: Periodically writes logs to a file and clears the memory buffer to avoid data loss.
- **System Information Logging**: Logs basic system information at the start of the session.
- **Extensibility**: Can be enhanced with additional features like stealth mode and remote logging.

## Encryption Key

The keylogger uses Fernet encryption, a symmetric encryption method that ensures the security of logged data. The encryption key is generated or loaded from a file (`key.key`).

- **Key Generation**: If a key doesn't exist, the keylogger generates a new one and stores it in `key.key`.
- **Key Loading**: If `key.key` already exists, it loads the key to use for encryption.

This key is crucial for both encrypting and decrypting the log file. Without this key, the logged data cannot be decrypted.

## Decryption

To view the encrypted logs, you need a decryption script that uses the same encryption key stored in `key.key`. This script will decrypt the log file, making the data human-readable.

## Possible Enhancements

While the keylogger is fully functional, it can be enhanced with the following features:

1. **Stealth Mode**: Run the script as a background process or a service to avoid detection, making it less visible to users.
2. **Remote Logging**: Send logs to a remote server or cloud storage, enabling remote monitoring and ensuring logs are not lost if the local machine is compromised.

## Implementing Stealth Mode and Remote Logging

### Stealth Mode

To make the keylogger run stealthily, especially on Windows, you can use `pythonw.exe` instead of `python.exe`, which suppresses the console window. Additionally, you can programmatically hide the console window using system calls.

### Remote Logging

You can set up a remote server to receive logs via HTTP POST requests. This allows for secure, remote storage of logs, enabling monitoring from different locations and ensuring logs are not lost even if the local machine is compromised.

## Final Thoughts

This remote encrypted keylogger is designed to be a robust tool for secure keylogging. With the addition of stealth mode and remote logging, it becomes even more powerful and versatile. These enhancements can be particularly useful in scenarios where security and stealth are paramount, such as in controlled environments or for legitimate monitoring purposes.

**Disclaimer**: This keylogger is provided for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always ensure you have proper authorization before deploying such tools.
