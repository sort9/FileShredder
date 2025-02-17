import tkinter as tk
from tkinter import messagebox, PhotoImage, filedialog, ttk
import string
from random import randint
import os
from datetime import datetime

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
    logFileDestruction()
    os.remove(filename)
    entry_file_input.delete("0", "end") # Remove entry box content after shred is complete
    shredCompleteMessage()

def createLogFile():
    currentTime = datetime.now()
    with open("events.log", "w") as file:
        file.write(str(currentTime) + " Log File Created")

def logFileDestruction():
    currentTime = datetime.now()
    with open("events.log", "a") as file:
        file.write("\n" + str(currentTime) + " " + str(filename) + " shredded")

def createFileShredTab(tab):
    label = ttk.Label(tab)
    label.pack(padx=20, pady=20)

    # File Input Entry Area
    global label_file_input
    label_file_input = tk.Label(tab, font=("Gill Sans MT", 11, "bold"), text="File to shred:")
    label_file_input.pack(side="left", padx=10, pady=10)
    label_file_input.config(bg="gray64")
    global entry_file_input
    entry_file_input = tk.Entry(tab, font=40)
    entry_file_input.pack(side="left")

    # Browse Button
    global browse_button
    browse_button = tk.Button(tab, text="Browse", font=40, command=browse)
    browse_button.pack(side="left", padx=5, pady=10)

    # Shred Button
    global shred_button
    shred_button = tk.Button(tab, text="Shred", font=40, command=shredFile)
    shred_button.pack(side="left",  padx=5, pady=10)

def createDirectoryShredTab(tab):
    label = ttk.Label(tab, text="PLACEHOLDER")
    label.pack(padx=20, pady=20)

def main():

    # Main window properties
    root = tk.Tk()
    root.title("Shredder Program")
    root.geometry("550x200") # Base window dimensions
    icon = PhotoImage(file='icons/314495_shredder_icon.png') # Set program icon
    root.iconphoto(True, icon)
    root.config(bg="gray64")

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)

    notebook.add(tab1, text="File Shredding")
    notebook.add(tab2, text="Directory Shredding")

    createFileShredTab(tab1)
    createDirectoryShredTab(tab2)

    notebook.pack(padx=10, pady=10, fill="both", expand=True)

    # Program opens opens in the center of the screen
    root.eval('tk::PlaceWindow . center')

    # Display Startup
    startupMessage()

    # Start Log File
    currentTime = datetime.now()
    createLogFile()

    root.mainloop()

if __name__ == "__main__":
    main()