import tkinter as tk
from tkinter import messagebox, PhotoImage, filedialog
import string
from random import randint
import os

# List of alphanumeric values to replace file contents with
alphanumeric = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
random_alphanumeric_index = randint(0, len(alphanumeric) - 1)

def startupMessage():
    messagebox.showinfo("IMPORTANT", "BE CAREFUL AS AFTER A FILE IS SHREDDED, RECOVERING IT WILL BE DIFFICULT") # Message box for when program start up is complete

def shredCompleteMessage():
    messagebox.showinfo("ALERT", "SHRED COMPLETE") # Message box for when shred operation is complete

def browse():
    global filename
    filename = filedialog.askopenfilename(filetypes=(("txt files", "*.txt"), ("All files", "*.*")))
    entry_file_input.insert(tk.END, filename)  # Insert the file path into the Entry widget

def shredFile():
    with open(filename, 'r') as file:
        global content
        content = file.read()
        characterCount = len(content)
    with open(filename, 'w') as file:
        for i in range(0, characterCount):
            content = file.write(alphanumeric[random_alphanumeric_index])
            file.flush() # To save file new file content without waiting for the buffer to flush and immediately save file to disk
    os.remove(filename)
    shredCompleteMessage()

# Main window properties
root = tk.Tk()
root.title("Shredder Program")
root.geometry("450x200") # Base window dimensions
icon = PhotoImage(file='icons/314495_shredder_icon.png') # Set program icon
root.iconphoto(True, icon)
root.config(bg="gray64")

# File Input Entry Area
label_file_input = tk.Label(root, font=("Gill Sans MT", 11, "bold"), text="File to shred:")
label_file_input.pack(side="left", padx=10, pady=10)
label_file_input.config(bg="gray64")
entry_file_input = tk.Entry(root, font=40)
entry_file_input.pack(side="left")

# Browse Button
browse_button = tk.Button(root, text="Browse", font=40, command=browse)
browse_button.pack(side="left", padx=5, pady=10)

# Shred Button
shred_button = tk.Button(root, text="Shred", font=40, command=shredFile)
shred_button.pack(side="left",  padx=5, pady=10)

# Program opens opens in the center of the screen
root.eval('tk::PlaceWindow . center')

# Display Startup
startupMessage()

# Run the main loop for then window
root.mainloop()