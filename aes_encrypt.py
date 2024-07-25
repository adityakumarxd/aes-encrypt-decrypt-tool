from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
import os

def encrypt_message(message, key):
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    return base64.b64encode(iv + encrypted_message).decode()

def main():
    message = input("Enter the message to encrypt: ")
    key = input("Enter the encryption key (16, 24, or 32 bytes long): ").encode()
    
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long.")

    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
