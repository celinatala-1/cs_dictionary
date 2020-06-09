#This file takes a txt file and converts it to json

import json

filename = "CS_Dictionary.txt"

#The dictionary where the lines from the text will be stored
dict1 = {}

def parse_files():
    with open(filename) as file:

        for line in file:
            if len(line.strip()) > 0:
                word, definition = line.strip().split(':')
                dict1[word.lower()] = definition.strip()
    out_file = open("Dictionary_File.json", "w")
    json.dump(dict1, out_file, indent = 4, sort_keys= True)
    out_file.close()
