import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

def encrypt_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift, 'encrypt')
    result_entry.delete(0, tk.END)  # Clear previous text
    result_entry.insert(0, encrypted_text)  # Show the encrypted text


def decrypt_text():
    text = text_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, shift, 'decrypt')
    result_entry.delete(0, tk.END)  # Clear previous text
    result_entry.insert(0, decrypted_text)  # Show the decrypted text

# Set up the main application window
app = tk.Tk()
app.title("Caesar Cipher GUI")
app.geometry("400x300")

# Input fields
tk.Label(app, text="Enter Text:").pack(pady=5)
text_entry = tk.Entry(app, width=30)
text_entry.pack(pady=5)

tk.Label(app, text="Shift Value:").pack(pady=5)
shift_entry = tk.Entry(app, width=10)
shift_entry.pack(pady=5)

# Buttons for Encrypt and Decrypt
encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_text)
decrypt_button.pack(pady=5)

# Result entry
tk.Label(app, text="Result:").pack(pady=5)
result_entry = tk.Entry(app, width=30)
result_entry.pack(pady=5)

# Run the application
app.mainloop()
