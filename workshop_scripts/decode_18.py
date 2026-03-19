input_file = "encrypted_data/18.txt"
output_file = "workshop_data/18.txt"

def decrypt(encrypted_message: str, key: int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

with open(input_file, "r") as f:
    encrypted_data = f.read()

# correct key found
key = 18

result = decrypt(encrypted_data, key)

with open(output_file, "w") as f:
    f.write(result)

print("Decoded using key:", key)