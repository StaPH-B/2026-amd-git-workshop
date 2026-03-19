#!/usr/bin/env python3 

import os

def decrypt(encrypted_message:str, key:int) -> str:
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        decrypted_char = chr((ord(char) - key) % 126)
        message += decrypted_char
    return message

if __name__ == "__main__":
  folder_path = "./encrypted_data/10.txt"
  answer_path = "./workshop_data/10.txt"
  with open(folder_path, "r") as file:
     content = file.read()
  encrypted_message_input = "K^MK^^M^^^M^^^QQQ^KK^^K^MM^^^^MMKKKQKKMK^^^^MMK^MMMKM^^QQKQ^MK^MMKMKK^KQMKMK^^KMKQQ^^KQ^QK^Q^MQKMKKKM^KQ^^^Q^MQ^QKMKKKM^Q^MK^MMKMKKK^MKK^^QKQK^MKQ^^QQKM^QKK^M^MQKKQQQKK^QQKQ^QQMKKM^QKMQ^QMMK^M^QMKKM^KKKKQK^QQQQM^^MKQQ^MMQQ^Q^MMMKMMKKKQQ^QQ^MKK^^K^QKKQM^QQ^QKK^QQQM^QKKKKM^QM^KMKK^M^^QKKK^MKKKKKKMM^QKMQQQKQ^QKQ^Q^M^KMMKQMKQMQMMKQKMQQQK^^MQQQQM^^MMMMMQQ^QMMQQ^K^Q^QMKMKKKQ^K^MKQQKKMQQQKMMQ^Q^QMMQQKQKM^^^QMM^^MMK^KKKQKQQQ^QM^^^M^^MM^Q^K^QK^MQKM^^QM^^MMKMKQ^^K^M^KMMQKQQKKMQKM^^^MQM^QKKQQ^Q^MQ^^QMK^^^M^QK^KM^QMMMMKKQM^KKQKKQQKM^^M^^MKQM^MKMKMMMM^^QKQKQKQMMQQ^MKK^QMKKMQQKQQKMMMQ^M^KQ^QQM^KM^K^^M^KMMKMKK^^KQK^K^MKQQM^KMMQQ^^^^QQKKMMKK^QKQKMKQKQ^KM^^Q^^MQKQQ^^QKMKK^^^QKMM^KMQ^M" 
  answer = decrypt(content, 10)
  print(answer)
  with open(answer_path, "w") as file:
     file.write(answer)

  with open(answer_path, 'r') as file:
     lines = file.read().splitlines()
     single_line_content = ''.join(line.strip() for line in lines)
    
  print(single_line_content)

  with open(answer_path, 'w') as output_file:
    output_file.write(single_line_content)
