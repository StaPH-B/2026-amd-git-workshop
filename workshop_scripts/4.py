# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

key = 4
input_file_path = f"encrypted_data/{key}.txt"
output_file_path = f"workshop_data/{key}.txt"

# decrypt the message
decrypted = None
with open(input_file_path, 'r') as file:
    encrypted = file.read()
    decrypted = decrypt(encrypted, 4)
    #print(decrypted)

# write the message to file
if decrypted is not None:
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(decrypted)
    

