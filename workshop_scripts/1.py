from pathlib import Path
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

text_file= Path("encrypted_data/1.txt")
output_file= Path("workshop_data/1.txt")

encrypted_text = text_file.read_text(encoding="utf-8")

result=decrypt(encrypted_message=encrypted_text, key=1)

output_file.write_text(result, encoding="utf-8")


