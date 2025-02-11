import tkinter as tk
from tkinter import messagebox, PhotoImage

def startup():
    messagebox.showinfo("IMPORTANT", "BE CAREFUL AS AFTER A FILE IS SHREDDED, RECOVERING IT WILL BE DIFFICULT")

# Main window properties
root = tk.Tk()
root.title("Shredder Program")
root.geometry("400x200") # base window dimensions
icon = PhotoImage(file='icons/314495_shredder_icon.png') # set program icon set
root.iconphoto(True, icon)

# File Input Entry Area
label_file_input = tk.Label(root, text="File to shred:")
label_file_input.pack()
entry_file_input = tk.Entry(root)
entry_file_input.pack()

# Display StartUP
startup()

# run the main loop for then window
root.mainloop()