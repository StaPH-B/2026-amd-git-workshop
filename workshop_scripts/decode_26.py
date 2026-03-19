# relative paths from this script's location
input_path = "encrypted_data/26.txt"
output_path = "workshop_data/26.txt"

# read encrypted text
with open(input_path, "r", encoding="utf-8") as f:
    encrypted_text = f.read()

# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

# decrypt
decrypted_text = decrypt(encrypted_text,26)

# write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(decrypted_text)

