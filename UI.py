import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import sarcasm
import pyperclip

answer = ""

def on_click():
    global answer

    text = text_field.get()
    answer = sarcasm.sarcasm(text)


    result.delete(1.0, tk.END)
    result.insert(tk.END, answer)

def copy():
    text_to_copy = result.get(1.0, tk.END).strip()
    pyperclip.copy(text_to_copy)
    copied.config(text="Copied to Clipboard!")
    



window = tk.Tk()
window.title("Sarcasm Generator")



label = tk.Label(window, text="Type a word or sentence:")
label.grid(row=0, column=0,padx=10,pady=10,sticky="w")

text_field = tk.Entry(window,width=75)
text_field.grid(row=1, column=0, padx=10, pady=0,sticky="w")

button = tk.Button(window,text="Generate Sarcasm",command=on_click)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=0, sticky="e")


result = tk.Text(window, height=5, width=70)
result.grid(row = 2,column=0,padx=10,pady=10,sticky="w")

copy_button = tk.Button(window, text="Copy to Clipboard",command=copy)
copy_button.grid(row=3, column=0, padx=10, pady=10,sticky="w")
copied = tk.Label(window,text="")
copied.grid(row=3,column=0,padx=10,pady=10)

window.mainloop()
