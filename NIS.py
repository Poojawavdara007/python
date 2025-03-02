from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import hashlib
import os

# --- AES Encryption ---
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return cipher.iv + ciphertext  # IV + Ciphertext

def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:16]  # Extract the IV
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    return decrypted_message

# --- Integrity Check ---
def calculate_checksum(data):
    return hashlib.sha256(data).hexdigest()

# --- Steganography ---
def bytes_to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_bytes(binary_data):
    byte_array = bytearray()
    for i in range(0, len(binary_data), 8):
        byte_array.append(int(binary_data[i:i + 8], 2))
    return bytes(byte_array)

def encode_image(image_path, message_bytes, output_image_path):
    img = Image.open(image_path)
    message_length = len(message_bytes)
    binary_message = format(message_length, '032b') + bytes_to_binary(message_bytes) + '1111111111111110'
    data_index = 0
    img_data = list(img.getdata())

    if len(binary_message) > len(img_data) * 3:
        raise ValueError("Image size is too small to encode the message.")

    new_img_data = []
    for pixel in img_data:
        if data_index < len(binary_message):
            new_pixel = list(pixel)
            for i in range(3):
                if data_index < len(binary_message):
                    new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1
            new_img_data.append(tuple(new_pixel))
        else:
            new_img_data.append(pixel)
    
    img.putdata(new_img_data)
    img.save(output_image_path)

def decode_image(image_path):
    img = Image.open(image_path)
    img_data = img.getdata()
    binary_data = ''.join(str(pixel[i] & 1) for pixel in img_data for i in range(3))

    # Extract message length
    message_length_bits = binary_data[:32]
    message_length = int(message_length_bits, 2)
    binary_message = binary_data[32:32 + (message_length * 8)]

    if '1111111111111110' not in binary_data:
        raise ValueError("Delimiter not found. Data might be corrupted.")
    
    return binary_message

# --- Chat Simulation ---
def sender_side():
    # Input message
    message = input("Enter your message to send: ")
    key = get_random_bytes(16)  # Generate AES-128 key
    encrypted_message = encrypt_message(message, key)
    original_checksum = calculate_checksum(encrypted_message)
    
    print("Message encrypted. Encoding into image...")
    input_image_path = input("Enter the path to the input image (e.g., nature.png): ")
    output_image_path = input("Enter the path to save the encoded image (e.g., encoded.png): ")

    encode_image(input_image_path, encrypted_message, output_image_path)
    print(f"Image saved at {output_image_path}.")
    return key, output_image_path, original_checksum

def receiver_side(key, encoded_image_path, original_checksum):
    print("Decoding the message from the image...")
    extracted_binary_data = decode_image(encoded_image_path)
    extracted_message_bytes = binary_to_bytes(extracted_binary_data)

    extracted_checksum = calculate_checksum(extracted_message_bytes)
    if original_checksum != extracted_checksum:
        print("Error: Data integrity check failed. The message is corrupted.")
    else:
        decrypted_message = decrypt_message(extracted_message_bytes, key)
        print("Message successfully decoded and decrypted!")
        print("Decrypted Message:", decrypted_message)

# --- Main Program ---
def chat_app():
    print("Welcome to the Steganographic Chat App!")
    print("1. Send a message")
    print("2. Receive a message")
    choice = input("Choose an option (1/2): ")
    if choice == '1':
        key, encoded_image_path, original_checksum = sender_side()
        print("\nShare the following details with the receiver:")
        print(f"Image Path: {encoded_image_path}")
        print(f"Encryption Key: {key.hex()}")
        print(f"Checksum: {original_checksum}")
    elif choice == '2':
        encoded_image_path = input("Enter the path to the encoded image: ")
        key_hex = input("Enter the encryption key provided by the sender: ")
        original_checksum = input("Enter the checksum provided by the sender: ")
        key = bytes.fromhex(key_hex)
        receiver_side(key, encoded_image_path, original_checksum)
    else:
        print("Invalid option. Exiting.")

if __name__ == "__main__":
    chat_app()
