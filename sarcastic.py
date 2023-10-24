import random
import tkinter as tk

#GUI

window = tk.Tk()
window.title("Sarcasm Generator")

text_box = tk.Entry(window)
text_box.pack(pady=10)

text_box.pack(anchor='center')

window.mainloop()

#Scripting

def sarcasm(text):
    text = text.lower()
    length = len(text)
    capital = []
    for i in range(len(text)):
        capital.append(random.randint(1, length - 1))

    for num in capital:
        text = text[:num] + text[num].upper() + text[num + 1:]

    return text

text = input("What would you like to capitalize?: \n")

output = sarcasm(text)

