# CipherTool

A simple Python tool to encrypt and decrypt text using a shuffled character mapping (substitution cipher).

## 📌 Description

This program generates a randomized key by shuffling letters, digits, punctuation, and space. It then uses this key to map each character in the input text for encryption and reverses the process for decryption.

## ⚙️ How It Works

- A pool of characters is created using letters, numbers, symbols, and space
- The pool is shuffled to generate a unique key
- Encryption replaces each character using the shuffled key
- Decryption maps it back to the original characters

## 🚀 Usage

Run the script with Python:

### macOS / Linux
```bash
python3 encryption_decryption.py
```

### Windows
```bash
python encryption_decryption.py
```

The program will:
1. Ask you to enter text to encrypt
2. Display the encrypted text
3. Ask you to enter text to decrypt
4. Display the decrypted text

## 📝 Example

```
Enter text to Encrypt: Hello World!
Encrypted Text:  ]qe##^]qe##

Enter text to Decrypt: ]qe##^]qe##
Decrypted Text:  Hello World!
```

## 🔧 Requirements

- Python 3.x
- Standard library modules: `random`, `string`

## ⚠️ Note

Since the encryption key is randomly generated each time the script runs, you must use the same script instance for both encryption and decryption. If you restart the script, a new key will be generated and previous encrypted text cannot be decrypted.