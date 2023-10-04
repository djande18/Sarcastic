import random

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

print(sarcasm(text))
