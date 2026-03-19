#!/usr/bin/env python3
import os

Text_id = "6"
KEY = 6

def decrypt(encrypted_message: str, key: int) -> str:
    """Decrypts a message by subtracting the key from each character."""
    message = ""
    for char in encrypted_message:
        # Use 32–126 printable ASCII range
        decrypted_char = (ord(char) - key)
        if decrypted_char < 32:  # wrap around printable ASCII
            decrypted_char += 95  # 126 - 32 + 1
        message += chr(decrypted_char)
    return message

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths relative to the script
input_file = os.path.join(script_dir, "..", "encrypted_data", f"{Text_id}.txt")
output_dir = os.path.join(script_dir, "..", "workshop_data")
output_file = os.path.join(output_dir, f"{Text_id}.txt")

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Check if input exists
if os.path.exists(input_file):
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    decrypted_text = decrypt(encrypted_text, KEY)

    with open(output_file, 'w') as f:
        f.write(decrypted_text)
    
    print(f"Success! Decrypted chunk {Text_id} and saved to {output_file}")
else:
    print(f"Error: {input_file} not found.")
