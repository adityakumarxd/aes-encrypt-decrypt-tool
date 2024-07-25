# AES Encryption/Decryption Tool

A Python tool for AES encryption and decryption using the `cryptography` library. This project provides two scripts: one for encrypting text and another for decrypting it using AES in CBC mode.

## Files

- **`aes_encrypt.py`**: Script for encrypting text using AES encryption.
- **`aes_decrypt.py`**: Script for decrypting AES-encrypted text.

## Usage

### Encryption

1. Run the encryption script:
    ```bash
    python aes_encrypt.py
    ```
2. Enter the text you want to encrypt.
3. Enter the encryption key (16, 24, or 32 bytes long).

The script will output the encrypted text.

### Decryption

1. Run the decryption script:
    ```bash
    python aes_decrypt.py
    ```
2. Enter the encrypted text you want to decrypt.
3. Enter the decryption key (16, 24, or 32 bytes long).

The script will output the decrypted text.

## Example

### Encryption Example

```bash
$ python aes_encrypt.py
Enter the message to encrypt: Hello, World!
Enter the encryption key (16, 24, or 32 bytes long): 1234567890123456
Encrypted message: <base64_encoded_encrypted_text>
```

### Decryption Example

```bash
$ python aes_decrypt.py
Enter the encrypted message to decrypt: <base64_encoded_encrypted_text>
Enter the decryption key (16, 24, or 32 bytes long): 1234567890123456
Decrypted message: Hello, World!
```

### Installation
```bash
pip install cryptography
```
