
# Load data
str9_encrypted = open("..\\encrypted_data\\9.txt").read()

# Decryption
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

str9_decrypted = decrypt(encrypted_message = str9_encrypted, key = 9)

# Save Decrypted data
with open("..\\workshop_data\\9.txt", "w") as file:
    file.write(str9_decrypted)

