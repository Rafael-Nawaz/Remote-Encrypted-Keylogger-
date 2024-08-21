from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Decrypt the log file
def decrypt_log_file(log_file_path):
    # Load the encryption key
    key = load_key()
    cipher = Fernet(key)

    # Read and decrypt the log file
    with open(log_file_path, "rb") as file:
        encrypted_data = file.readlines()

    # Decrypt each line and print
    for encrypted_line in encrypted_data:
        decrypted_line = cipher.decrypt(encrypted_line).decode()
        print(decrypted_line)

# Path to your encrypted log file
log_file_path = "log.txt"

# Decrypt and display the log file
decrypt_log_file(log_file_path)
