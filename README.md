# Caesar Cipher Encryption/Decryption Tool
![Dalle2_ART](docs/dalle2.png)
Artwork created by Dalle2 AI 


## Project Overview
This Python script serves as a Caesar Cipher encryption and decryption tool. The purpose is to encode and decode messages using the basic American Standard Code for Information Interchange (ASCII). The script utilizes the sys package for input handling.

## Code Details
The script employs `if`, `else`, and `elif` functions for handling user choices. The `if` statement checks whether the user wants to encrypt or decrypt the message. If encrypting, it enters the corresponding line of code; if decrypting, it enters another line of code. The `elif` function is used for additional conditions. Additionally, basic `for` loops are used for both encryption and decryption processes. These loops iterate through each character in the input message, applying the Caesar Cipher algorithm. The `ord` function is used to convert characters to their corresponding ASCII values, and the `chr` function is used to convert ASCII values back to characters. The `''.join` function is also utilized to concatenate the characters back into a string, providing a more readable format for the final result.

## Limitations
- The encoded message appearance can vary based on the chosen key, potentially resulting in non-alphabetic characters.
- A temporary fix is implemented by instructing users to copy and paste the encoded message for future decryption.
- Considerations for improving the user experience, such as finding alternatives to manual copying and pasting, are mentioned.

## Future Steps
- Explore solutions to make the encoding and decoding process more user-friendly without manual copying.
- Consider adapting the code for use in a Telegram bot to provide a more streamlined and accessible experience.

## How to Use
1. Run the script in a Python environment.
```bash
python caesar_cipher.py
```
2. Choose whether to encrypt or decrypt a message by entering 'E' or 'D' respectively.
3. If encrypting, enter the message to be encoded and a key for encryption.
4. If decrypting, enter the message to be decoded and the encryption key used.
5. Copy and save the resulting encrypted or decrypted message.
6. The program prompts whether you want to use the Caesar Cipher tool again. Respond with 'Y' to continue, or 'N' to exit.
