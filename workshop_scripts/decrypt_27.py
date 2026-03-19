import os

my_key=27

# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - my_key) % 126)
        message += decrypted_char
    return message


def get_relative_path(my_path:str):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, my_path, f"{my_key}.txt")


def main():
    in_path = get_relative_path("encrypted_data")
    out_path = get_relative_path("workshop_data")

    encrypted_file = open(in_path, "r")

    with open(out_path, "w") as decrypted_file:
        decrypted_file.write(decrypt(encrypted_file.read()))


if __name__ == "__main__":
    main()
