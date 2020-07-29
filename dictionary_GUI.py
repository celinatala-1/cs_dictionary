#A basic dictionary program that reads from a document. 
# User can search for a word, and the definition will appear

from file_parse import *
import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import *
from tkinter import messagebox


#loading our json file into our dictionary
parse_files()
dictionary = json.load(open("Dictionary_File.json"))

def get_word(word):
    word = word.lower()
    x = "Word: " + word
    Label(new, text=x, wraplength=395).pack(anchor=W)
    y = "Definition: " + dictionary[word]
    Label(new, text=y, wraplength=395).pack(anchor=W)

def none():
    messagebox.showerror(new, "The Word doesn't exist in our dictionary. Please Try again")

#gets the definition of a word
def get_definition():
    global new
    word = w.get()
    word = word.lower()
    # root.withdraw()
    new = Toplevel()
    new.geometry('400x200')
    #converts to lowercase
    close_match = get_close_matches(word, dictionary.keys())
    #if the word is in the dictionary return definition
    if word in dictionary:
        get_word(word)
    #for getting close matches of a word
    elif len(close_match) > 0:
        c = Canvas(new, height = 200, width = 400)
        Label(c, text = "There was a spelling mistake, choose correct word").pack(anchor = CENTER)
        b = Canvas(new, height = 200, width = 400)
        for x in close_match:
            Button(b, text = x, wraplength = 100, command = lambda : get_word(x)).pack(side = LEFT)
        Button(b, text = "None", command = none).pack(side = LEFT)
        c.pack()
        b.pack()
    else:
        none()

root = tk.Tk()
Label(root, text = "Enter Word").pack(side = LEFT)
w = Entry(root)
w.pack(side = LEFT)
Button(root, text = "Go", command = get_definition).pack()

root.mainloop()
