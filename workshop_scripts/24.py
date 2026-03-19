#!/usr/bin/env python3


id=24


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, data: str) -> None:
    with open(path, "w") as f:
        f.write(data)


def decrypt(encrypted_message: str, key: int) -> str:
    chars = []
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - key) % 126)
        chars.append(decrypted_char)
    return ''.join(chars)


def main():
        infile  = f"encrypted_data/{id}.txt"
        outfile = f"workshop_data/{id}.txt"

        encrypted = read_file(infile)
        decrypted = decrypt(encrypted, id)
        write_file(outfile, decrypted)


main()

