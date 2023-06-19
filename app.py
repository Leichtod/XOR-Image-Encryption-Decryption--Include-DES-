from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sys


def select(entry, ok):
    filename = ""
    if ok == 'r':
        filename = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(
            ("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")))
    elif ok == 'b':
        filename = filedialog.askdirectory()
    elif ok == 't':
        filename = filedialog.askopenfilename(initialdir="/", title="Select Txt File",
                                              filetypes=(("TXT Files", "*.txt"), ("All Files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def create(frame, label_text, row, ok):
    label = tk.Label(frame, text=label_text)
    label.grid(column=1, row=row, padx=10, pady=10)

    entry = tk.Entry(frame)
    entry.grid(column=2, row=row, padx=10, pady=10)

    button = tk.Button(frame, text="Select", command=lambda: select(entry, ok))
    button.grid(column=3, row=row, padx=10, pady=10)

    return entry


def encrypt():
    encryptList = [image.get(), encryptDES.get(), encryptKey.get(), encryptDES2.get(), encryptKey2.get(),
                   encryptedImage.get()]
    for i in range(0, len(encryptList)):
        if len(encryptList[i]) == 0:
            messagebox.showinfo("Info", "Do not leave any blank space!")
            return
    sI = "\n".join(encryptList)
    with open("file_paths/encrypt.txt", "w", encoding="utf-8") as f:
        f.write(sI)
    import encrypt
    messagebox.showinfo("Info", "Encryption Completed!")
    with open("file_paths/decrypt.txt", "w", encoding="utf-8") as f:
        f.write("")
    sys.exit()


def decrypt():
    decryptList = [enImage.get(), decryptDES.get(), decryptKey.get(), decryptDES2.get(), decryptKey2.get(),
                   decryptImage.get()]
    for i in range(0, len(decryptList)):
        if len(decryptList[i]) == 0:
            messagebox.showinfo("Info", "Do not leave any blank space!")
            return
    sK = "\n".join(decryptList)
    with open("file_paths/decrypt.txt", "w", encoding="utf-8") as f:
        f.write(sK)
    import decrypt
    messagebox.showinfo("Info", "Decryption Completed!")
    with open("file_paths/decrypt.txt", "w", encoding="utf-8") as f:
        f.write("")
    sys.exit()


window = tk.Tk()
window.title("Image Encryption and Decryption Application")
window.iconbitmap("lch.ico")

tab_control = ttk.Notebook(window)

# Tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Encryption')
image = create(tab1, "Import Image:", 0, 'r')
encryptDES = create(tab1, "Extract DES Key: ", 1, 'b')
encryptDES2 = create(tab1, "Extract DES Key2: ", 2, 'b')
encryptKey = create(tab1, "Extract Key:", 3, 'b')
encryptKey2 = create(tab1, "Extract Key2:", 4, 'b')
encryptedImage = create(tab1, "Extract the Encrypted Image:", 5, 'b')

# Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Decryption')
enImage = create(tab2, "Import the Encrypted Image:", 0, 'r')
decryptDES = create(tab2, "Import DES Key: ", 1, 't')
decryptDES2 = create(tab2, "Import DES Key2: ", 2, 't')
decryptKey = create(tab2, "Import Key", 3, 't')
decryptKey2 = create(tab2, "Import Key2", 4, 't')
decryptImage = create(tab2, "Extract the Decrypted Image:", 5, 'b')

tab_control.pack(expand=1, fill='both')

eButton = tk.Button(tab1, text="Encryption Start", command=encrypt)
dButton = tk.Button(tab2, text="Decryption Start", command=decrypt)
eButton.grid(column=2, row=6, padx=10, pady=10)
dButton.grid(column=2, row=6, padx=10, pady=10)

window.resizable(0, 0)
window.mainloop()
