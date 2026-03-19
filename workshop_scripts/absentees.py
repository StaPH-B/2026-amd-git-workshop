#!/usr/bin/env python3

ABSENTEES = [8, 12, 13, 28]


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
    for student_id in ABSENTEES:
        infile  = f"encrypted_data/{student_id}.txt"
        outfile = f"workshop_data/{student_id}.txt"

        encrypted = read_file(infile)
        decrypted = decrypt(encrypted, student_id)
        write_file(outfile, decrypted)


if __name__ == "__main__":
    main()