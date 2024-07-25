from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

def decrypt_message(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message)

    iv = encrypted_message[:16]
    encrypted_message = encrypted_message[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()

    return message.decode()

def main():
    encrypted_message = input("Enter the encrypted message to decrypt: ")
    key = input("Enter the decryption key (16, 24, or 32 bytes long): ").encode()
    
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long.")

    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
