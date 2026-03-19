import os

def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

input_path = "encrypted_data/20.txt"
output_path = "workshop_data/20.txt"

os.makedirs("workshop_data", exist_ok=True)

with open(input_path, "r") as f:
    encrypted = f.read().strip()

decoded = decrypt(encrypted, 20)

with open(output_path, "w") as f:
    f.write(decoded)
    