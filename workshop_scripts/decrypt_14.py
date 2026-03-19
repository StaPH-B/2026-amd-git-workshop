#!/usr/bin/env python3

"""Script to decrypt 14.txt file for GitHub workshop"""


def main():
    # read in txt file from encrypted_data
    with open('encrypted_data/14.txt', 'r') as encrypted_file:
        encrypted_message = encrypted_file.read()

        # decrypt with key 14
        message = decrypt(encrypted_message, 14)

    # write txt file to workshop_data
    with open('workshop_data/14.txt', 'w') as decrypted_file:
        decrypted_file.write(message)


def decrypt(encrypted_message: str, key: int) -> str:
    """Simple function to decrypt a string by shifting the ascii code by some value (key)"""
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message


if __name__ == "__main__":
    main()
