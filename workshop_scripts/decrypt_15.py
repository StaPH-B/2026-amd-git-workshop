from pathlib import Path

# relative paths from this script's location
input_path = Path("encrypted_data/15.txt")
output_path = Path("workshop_data/15.txt")

# read encrypted text
encrypted_text = input_path.read_text(encoding="utf-8")

# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

# decrypt
decrypted_text = decrypt(encrypted_text, 15)

# write output
output_path.write_text(decrypted_text, encoding="utf-8")

