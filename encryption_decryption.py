import random
import string

letter_pool = " " + string.ascii_letters + string.digits + string.punctuation

all_letters = list(letter_pool)
key = all_letters.copy()

random.shuffle(key)

# Encryption
def encryption(text):
    encrypted_text = ""

    for letter in text:
        index = all_letters.index(letter)
        encrypted_text += key[index] 
    
    return encrypted_text

print()

#Decryption
def decryption(text):
    decrypted_text = ""

    for letter in text:
        index = key.index(letter)
        decrypted_text += all_letters[index] 
    
    return decrypted_text

print("Encrypted Text: ", encryption(input("Enter text to Encrypt: ")))
print("Decrypted Text: ", decryption(input("Enter text to Decrypt: ")))
