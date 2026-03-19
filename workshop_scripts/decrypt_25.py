import os

# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

def main():
    # Configuration
    input_folder = "./encrypted_data"
    output_folder = "./workshop_data"
    filename = "25.txt"
    key = 25

    # 1. Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # 2. Define full file paths
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # 3. Process the file
    if os.path.exists(input_path):
        try:
            # Read the encrypted file
            with open(input_path, 'r', encoding='utf-8') as f:
                encrypted_content = f.read()

            # Decrypt using your function and the key 25
            decrypted_content = decrypt(encrypted_content, key)

            # Write to output file using the same name
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(decrypted_content)

            print(f"Success! Decrypted {filename} and saved to {output_path}")

        except Exception as e:
            print(f"An error occurred during file processing: {e}")
    else:
        print(f"Error: The file '{input_path}' was not found.")

if __name__ == "__main__":
    main()
