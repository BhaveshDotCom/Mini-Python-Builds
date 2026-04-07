# CipherTool  

A simple Python tool to encrypt and decrypt text using a shuffled character mapping (substitution cipher).  

---

## 📌 Description  
This program generates a randomized key by shuffling letters, digits, punctuation, and space.  
It then uses this key to map each character in the input text for encryption and reverses the process for decryption.  

---

## ⚙️ How It Works  
- A pool of characters is created using letters, numbers, symbols, and space  
- The pool is shuffled to generate a unique key  
- Encryption replaces each character using the shuffled key  
- Decryption maps it back to the original characters 