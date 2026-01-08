# APHL Git Workshop Challenge

This is a puzzle challenge where some text is encrypted using an ASCII shift. Each person will receive a key and will have to write a small script that when run will decrypt the data and output their chunk of the sequence data to the `workshop_data` location in the repository. Their script will be included in a large batch operation run by GitHub actions that will result in everyone's data being decrypted and displayed.

## Introduction
[StaPH-B/2026-amd-git-workshop](https://github.com/StaPH-B/2026-amd-git-workshop) contains some text that has been broken into chunks and encrypted. For this exercise, you will write a simple script to decode your chunk and contribute that script to the shared repository.

## Procedure

Below are the rough steps needed to complete this assignment, with specific details omitted. Please attempt each step and ask an instructor if you have questions or need help.

1. Fork the shared training repository to your GitHub account.
2. Clone the repository to your preferred development environment.
3. Create a script in **bash** or **python** in the `workshop_scripts` directory which decodes your chunk stored in the `encrypted_data` folder and outputs the decoded text into the `workshop_data` directory using the `[key].txt` format i.e. `2.txt`.
4. Commit the new script on your fork of the repository.
5. Push the new commit to your fork on GitHub.
6. Create pull request in the [StaPH-B/2026-amd-git-workshop](https://github.com/StaPH-B/2026-amd-git-workshop) on GitHub to merge changes from your fork into the shared training repository.
7. Review and approve an open pull request from someone else in the training repository
8. Once approved, an instructor will merge each pull request into the shared training repository.
9. A GitHub action workflow will run all of the scripts, produce the decrypted output, and inspects the output to see if all chunks were decrypted successfully.
10. If the output is not 100% decrypted, work as a group to identify any issues, patch them, and repeat steps 4-9 to check the results again!


## Example Decryption function

```
python
# Simple function to decrypt a string by shifting the ascii code by some value (key)
def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message
```