from tkinter import *
from itertools import chain, combinations, permutations
from math import *
import tkinter as tk
import tkinter.scrolledtext as tkscrolled

# Setup
main = Tk()
main.title('Combinations')
main.geometry("1000x1000")

# Get permutations
def all_subsets(ss):
    return chain(*map(lambda x: permutations(ss, x), range(0, len(ss)+1)))

# All input combinations
def only_words(words):
    for subset in all_subsets(words):
        out.insert(END, ' '.join(subset)+"\n")
 
def words_and_must_have(words, include):
    for subset in all_subsets(words):
        combo = " ".join(subset)+"\n"
        if all([word in combo for word in include.split()]):
            out.insert(END, combo)
    
def words_and_length(words, length):
    for subset in all_subsets(words):
        combo = " ".join(subset)+"\n"
        if len(subset) == length:
            out.insert(END, combo)

def words_length_must_have(words, include, length):
    for subset in all_subsets(words):
        combo = " ".join(subset)+"\n"
        if all([word in combo for word in include.split()]):
            if len(subset) == length:
                    out.insert(END, combo)

# Button "Go" functionality
def go():
    """ 4 cases:
    1) only words
    2) Words + must have
    3) Words + length
    4) OWrds + must have + length
    """
    #Clear textbox
    out.delete(1.0, END)
    #If empty input
    if len(words.get().split()) < 1:
        out.insert(END, "You must enter words to get the combinations!")
    # If only words
    elif len(words.get().split()) > 0 and len(must_have.get().split()) < 1 and len(length.get().split()) < 1:
        only_words(words.get().split())
    # If words and must have
    elif len(words.get().split()) > 0 and len(must_have.get().split()) > 0 and len(length.get().split()) < 1:
        print(must_have.get())
        words_and_must_have(words.get().split(), must_have.get())
    # If words and length
    elif len(words.get().split()) > 0 and len(must_have.get().split()) < 1 and len(length.get().split()) > 0:
        print("got in length")
        words_and_length(words.get().split(), int(length.get()))
    # If words, length and must have
    elif len(words.get().split()) > 0 and len(must_have.get().split()) > 0 and len(length.get().split()) > 0:
        words_length_must_have(words.get().split(), must_have.get(), int(length.get()))
    else:
        out.insert(END, "There was an error, please clear and try again.")

# Button clear
def clear():
    length.delete(0, END)
    must_have.delete(0, END)
    words.delete(0, END)
    out.delete(1.0, END)

# UI setup
main.geometry('500x500')
Label(main, text = "Words: ").grid(row=0)
Label(main, text = "Must have: ").grid(row=1)
Label(main, text = "Length: ").grid(row=2)

# Text inputs and box
words = Entry(main, width=50)
must_have = Entry(main, width=50)
length = Entry(main, width=50)
out = tkscrolled.ScrolledText(main)

# Text box setup
words.grid(row=0, column=1)
must_have.grid(row=1, column=1)
length.grid(row=2, column=1)
out.grid(row=7, column=1)
out.place(x=65, y=80, height=350, width=400)

# Buttons
Button(main, text='  Go  ', command=go).grid(row=0, column=5, sticky=W, padx=(10, 0))
Button(main, text='Clear', command=clear).grid(row=0, column=6, sticky=W, padx=(10, 0))
Button(main, text='Quit', command=main.destroy).place(x=420, y=440)

mainloop()