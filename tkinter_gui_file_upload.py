import tkinter as tk
from tkinter import filedialog
import hashlib


def copy_button():
    window.clipboard_clear()
    window.clipboard_append(checksum_entry.get())
    label_file_explorer.configure(
        text="Checksum copies to clipboard. Save it to somewhere safe before closing this window")


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(
                                              ("All files",
                                               "*.*"),
                                          ))

    # if we click on upload file button but then click cancel
    if not filename or not isinstance(filename, str):
        label_file_explorer.configure(text="No file uploaded.")
        return

    # read file in binary mode.
    with open(filename, "rb") as input_file:
        # text is bytes type in rb mode
        text = input_file.read()

    # checksum of whole text at once
    checksum = hashlib.sha256(text).hexdigest()
    print("complete file checksum: " + checksum)  # type is string

    # calculating checksum for one byte at a time and updating the hash
    byte_count = len(text)
    byte_chunks = [text[i: i + 2] for i in range(0, byte_count, 2)]
    # new hash object with sha256 algorithm
    h = hashlib.new('sha256')
    for single_byte in byte_chunks:
        h.update(single_byte)

    # final checksum of hash
    combined_checksum = h.hexdigest()

    print("byte by byte checksum: " + combined_checksum)

    msg = "File Opened: " + filename
    # Change label contents
    label_file_explorer.configure(text=msg)

    # clear the entry field before inserting checksum there
    checksum_entry.delete(0, tk.END)
    checksum_entry.insert(0, checksum)


# starting program
window = tk.Tk()
window.title('File Checksum Generator')
title = tk.Label(text="Generate file checksum. Upload a file.", pady=20)
title.pack()

label_file_explorer = tk.Label(window, text="", width=100, height=4, pady=10)
button_explore = tk.Button(window, text="Browse Files", command=browse_files, pady=20)
button_copy = tk.Button(window, text="Copy Checksum", command=copy_button, pady=10)
button_exit = tk.Button(window, text="Exit", command=exit, pady=10)

checksum_entry = tk.Entry(width=70)
checksum_entry.insert(0, "Checksum will appear here")

button_explore.pack()
label_file_explorer.pack()
checksum_entry.pack()
button_copy.pack()
button_exit.pack()

window.mainloop()
