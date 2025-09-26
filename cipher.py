import random
import string

# Define characters
chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)

# Generate key
key = chars.copy()
random.shuffle(key)


# Encrypt function
def encrypt(message):
    cipher_text = ""
    for letter in message:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text


# Decrypt function
def decrypt(cipher):
    plain_text = ""
    for letter in cipher:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text


# Main Program
plain_text = input("Enter the message to encrypt: ")
cipher_text = encrypt(plain_text)
print(f"\nOriginal Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")

# Decryption
decrypt_text = decrypt(cipher_text)  # directly decrypting without asking input again
print(f"Decrypted Message: {decrypt_text}")

