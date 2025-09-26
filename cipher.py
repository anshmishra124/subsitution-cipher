import random
import string
import json
import argparse
import os

# ----------------------------
# Define available characters
# ----------------------------
CHARS = " " + string.punctuation + string.ascii_letters + string.digits
CHARS = list(CHARS)


# ----------------------------
# Generate a random key
# ----------------------------
def generate_key():
    key = CHARS.copy()
    random.shuffle(key)
    return key


# ----------------------------
# Save key to a file
# ----------------------------
def save_key(key, filename="key.json"):
    with open(filename, "w") as f:
        json.dump(key, f)


# ----------------------------
# Load key from a file
# ----------------------------
def load_key(filename="key.json"):
    if not os.path.exists(filename):
        raise FileNotFoundError("Key file not found! Generate and save a key first.")
    with open(filename, "r") as f:
        return json.load(f)


# ----------------------------
# Encrypt a message
# ----------------------------
def encrypt(message, key):
    cipher_text = ""
    for letter in message:
        index = CHARS.index(letter)
        cipher_text += key[index]
    return cipher_text


# ----------------------------
# Decrypt a message
# ----------------------------
def decrypt(cipher, key):
    plain_text = ""
    for letter in cipher:
        index = key.index(letter)
        plain_text += CHARS[index]
    return plain_text


# ----------------------------
# Command-Line Interface
# ----------------------------
def main():
    parser = argparse.ArgumentParser(description="Substitution Cipher Encryption Tool")
    parser.add_argument("-e", "--encrypt", help="Message to encrypt")
    parser.add_argument("-d", "--decrypt", help="Message to decrypt")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate a new key")
    parser.add_argument("-k", "--keyfile", default="key.json", help="Path to key file")

    args = parser.parse_args()

    if args.generate:
        key = generate_key()
        save_key(key, args.keyfile)
        print(f"[+] New key generated and saved to {args.keyfile}")
        return

    try:
        key = load_key(args.keyfile)
    except FileNotFoundError as e:
        print(e)
        return

    if args.encrypt:
        cipher_text = encrypt(args.encrypt, key)
        print(f"Original: {args.encrypt}")
        print(f"Encrypted: {cipher_text}")

    elif args.decrypt:
        plain_text = decrypt(args.decrypt, key)
        print(f"Encrypted: {args.decrypt}")
        print(f"Decrypted: {plain_text}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
