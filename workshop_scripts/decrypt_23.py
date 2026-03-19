key = 23
  
input_file = "encrypted_data/23.txt"
output_file = "workshop_data/23.txt"

def decrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) - key)
    return result

with open(input_file, "r") as f:
    encrypted = f.read()

decrypted = decrypt(encrypted, key)

with open(output_file, "w") as f:
    f.write(decrypted)

print("Decryption complete for 23.txt.")
