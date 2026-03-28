Here’s a clean, professional **GitHub README.md** you can directly paste into your repo (edit-friendly, well-structured, and impressive 👇)

---

# 🔐 Steganographic Chat App (AES + Image Hiding)

A secure communication system that combines **AES encryption** with **image steganography** to hide secret messages inside images.

This project ensures:

* 🔒 **Confidentiality** (AES encryption)
* 🕵️ **Stealth** (hidden inside images)
* ✅ **Integrity** (SHA-256 checksum verification)

---

## 🚀 Features

* AES-128 encryption (CBC mode)
* Secure random key generation
* Message embedding inside images (LSB technique)
* Data integrity check using SHA-256
* Sender & Receiver simulation
* Simple CLI-based interface

---

## 🧠 How It Works

### 🔹 Sender Side

1. User enters a message
2. Message is encrypted using AES
3. Checksum is generated
4. Encrypted message is hidden inside an image
5. Sender shares:

   * Encoded image
   * Encryption key
   * Checksum

### 🔹 Receiver Side

1. Extract hidden data from image
2. Verify checksum
3. Decrypt message using AES key
4. Display original message

---

## 📂 Project Structure

```
📁 steganographic-chat-app
│── main.py              # Main application
│── README.md           # Documentation
│── sample_images/      # Input/output images (optional)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/steganographic-chat-app.git
cd steganographic-chat-app
```

### 2. Install dependencies

```bash
pip install pycryptodome pillow
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

### Choose mode:

#### 📤 Send a Message

* Enter your secret message
* Provide input image path
* Output encoded image will be generated

#### 📥 Receive a Message

* Provide encoded image path
* Enter key & checksum
* Message will be decrypted

---

## 🔑 Security Details

### AES Encryption

* Mode: CBC (Cipher Block Chaining)
* Key Size: 128-bit
* Random IV used for each encryption

### Steganography

* Uses **LSB (Least Significant Bit)** technique
* Stores data in RGB pixel values

### Integrity Check

* SHA-256 checksum ensures data is not altered

---

## ⚠️ Limitations

* Image must be large enough to store message
* Key sharing must be done securely
* Not resistant to advanced steganalysis

---

## 💡 Future Improvements

* GUI (Tkinter / React frontend)
* Support for audio/video steganography
* Public-key encryption (RSA)
* Secure key exchange (Diffie-Hellman)
* Compression before encoding
* Multi-user chat system

---

## 🧪 Example

```
Message: Hello World
Encrypted → Hidden in image → Sent

Receiver:
Extract → Verify → Decrypt → Output: Hello World
```

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**PoojaCodesX**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it


