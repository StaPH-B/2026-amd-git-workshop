#!/usr/bin/env python3
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

def main():
    file_path = "encrypted_data/21.txt" # The path to your file
    student_key = 21 # The student key for decryption

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content_string = f.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    decrypted_message = decrypt(file_content_string, student_key)
    print("Decrypted message:", decrypted_message)

    file_output_path = "workshop_data/" + str(student_key) + ".txt"
    with open(file_output_path, "w") as file:
        file.write(decrypted_message)

if __name__ == "__main__":
    main()