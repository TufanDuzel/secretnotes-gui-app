# Secret Notes GUI App

## Overview
Secret Notes is a simple GUI-based application that allows users to store encrypted notes securely. Users can enter a title, a secret message, and a master key for encryption. The encrypted message is then stored in a text file. Later, users can retrieve and decrypt their notes by providing the correct encrypted text and master key.

## Features
- **Secure Note Storage**: Encrypts and stores notes securely in a file.
- **Custom Encryption Key**: Uses a user-defined master key to encrypt and decrypt messages.
- **Simple GUI Interface**: Built with Tkinter for ease of use.
- **Persistent Storage**: Saves encrypted messages to a file for future retrieval.

## How It Works
1. **Save & Encrypt**:
   - Enter a **Title** for the note.
   - Enter a **Secret Message** to be encrypted.
   - Enter a **Master Key** for encryption.
   - Click **"Save & Encrypt"** to encrypt the message and save it to a file.

2. **Decrypt a Note**:
   - Copy the **Encrypted Message** from the text file.
   - Enter the **Encrypted Message** in the app.
   - Enter the **Master Key** that was used for encryption.
   - Click **"Decrypt"** to reveal the original message.

## Installation
### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/TufanDuzel/secretnotes-gui-app.git
cd secretnotes-gui-app
```

### Install Required Dependencies
```bash
pip install pillow
```

## Usage
Run the application using:
```bash
python secretnotes.py
```

## File Storage
The application stores encrypted messages in a text file (`secretnotes.txt`). Each entry consists of:
```
Title
EncryptedMessage
```

## Example
### Encrypting a Note:
**Input:**
- Title: `My Secret`
- Secret Message: `This is a hidden message!`
- Master Key: `Spain`

**Encrypted Output (Stored in the file):**
```
My Secret
wpzCkMOYw4rDnMOWwpDD1cOYwo7Cus...
```

### Decrypting a Note:
**Input:**
- Encrypted Message: `wpzCkMOYw4rDnMOWwpDD1cOYwo7Cus...`
- Master Key: `Spain`

**Decrypted Output:**
```
This is a hidden message!
```

## Technologies Used
- **Python**: Programming language.
- **Tkinter**: GUI framework.
- **Pillow**: Image handling for UI elements.
- **Base64**: Encoding for encryption.

## Contributing
Feel free to fork the repository and submit pull requests. Suggestions and improvements are welcome!
