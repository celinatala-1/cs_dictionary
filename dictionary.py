#A basic dictionary program that reads from a document. User can search for a word, and the definition will appear

from file_parse import *
import json
from difflib import get_close_matches

#loading our json file into our dictionary
parse_files()
dictionary = json.load(open("Dictionary_File.json"))

#gets the definition of a word
def get_definition(word):
    #converts to lowercase
    word = word.lower()

    #if the word is in the dictionary return definition
    if word in dictionary:
        return dictionary[word]
    #for getting close matches of a word
    close_match = get_close_matches(word, dictionary.keys())
    if len(close_match) > 0:
        print("Is your word in this list? Press the number corresponding to the right word and N for no")
        s = ""
        #printing out the list of potential words
        for i in range (len(close_match)):
            if i == len(close_match) -1:
                s+=close_match[i]
            else:
                s+=close_match[i] + ", "
        print(s)
        x = input()
        if x == "n":
            return("The word doesn't exist. Please try again")
        x = int(x)
        if x in range (len(close_match)+1):
            word = close_match[x-1]
            return dictionary[word]
        else:
            return "We don't understand your entry"
    else:
        return "The Word doesn't exist. Please Try again"

while True:
    word = input("Enter a Word (type 'quit' to stop) : ")
    if word == "quit":
        break
    print(get_definition(word))
