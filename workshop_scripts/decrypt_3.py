import os
Text_id= "3"
KEY = 3

def decrypt(encrypted_message, key):
    message = ""
    for char in encrypted_message:
        message += chr((ord(char) - key) % 126)
    return message

input_file = os.path.join("encrypted_data", f"{Text_id}.txt")
output_file = os.path.join("workshop_data", f"{Text_id}.txt")

if os.path.exists(input_file):
    with open(input_file, 'r') as f:
        encrypted_text = f.read()

    decrypted_text = decrypt(encrypted_text, KEY)

    os.makedirs("workshop_data", exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(decrypted_text)
    
    print(f"Success! Decrypted chunk {Text_id} and saved to {output_file}")
else:
    print(f"Error: {input_file} not found.") 
