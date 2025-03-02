from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64

# Functions
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt():
    title = title_entry.get()
    message = message_text.get("1.0", END) # Start from 1. row and 1. character, get until to the end.
    key = key_entry.get()

    if len(title) == 0 or len(message) == 0 or len(key) == 0:
        messagebox.showwarning(title="Error!", message="Please enter all info.") # Show error.
    else:
        #encryption
        message_encrypted = encode(key, message)

        try:
            with open("secretnotes.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("secretnotes.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0, END) # Delete the title everytime.
            message_text.delete("1.0", END) # Delete the message everytime.
            key_entry.delete(0, END) # Delete the key everytime.

def decrypt():
    message_encrypted = message_text.get("1.0", END)
    key = key_entry.get()

    if len(message_encrypted) == 0 or len(key) == 0:
        messagebox.showwarning(title="Error!", message="Please enter all info.")
    else:
        try:
            message_decrypted = decode(key, message_encrypted)
            message_text.delete("1.0", END)
            message_text.insert("1.0", message_decrypted) # To add the message into text box.
        except:
            messagebox.showwarning(title="Error!", message="Please enter encrypted text.")

# UI
# Window
window = Tk()
window.title("Secret Notes")
window.minsize(width=300, height=575)

# Photo
image = Image.open("secretnotes-logo.png") # Opening the photo with Pillow.
image = image.resize((120, 120)) # Resize
photo = ImageTk.PhotoImage(image) # Make it suitable for Tkinter.

photo_label = Label(window, image=photo) # Create a label to show the photo in the screen.
photo_label.pack()

# Label (Title)
title_label = Label(text="Enter Your Title", font=("Arial", 10, "bold"))
title_label.config(padx=5, pady=5)
title_label.pack()

# Entry (Title)
title_entry = Entry(width=30)
title_entry.pack(padx=5, pady=5)

# Label (Message)
message_label = Label(text="Enter Your Secret", font=("Arial", 10, "bold"))
message_label.config(padx=5, pady=5)
#message_label.place(x= 95, y= 200)
message_label.pack()

# Text (Message)
message_text = Text(width=25, height=13)
message_text.pack()

# Label (Key)
key_label = Label(text="Enter Master Key", font=("Arial", 10, "bold"))
key_label.config(padx=5, pady=5)
key_label.pack()

# Entry (Key)
key_entry = Entry(width=30)
key_entry.pack(padx=5, pady=5)

# Button (Save_And Encrypt)
save_encrypt_button = Button(text="Save & Encrypt", command=save_and_encrypt)
save_encrypt_button.pack()

# Button (Decrypt)
decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()

window.mainloop()