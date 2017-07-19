#!/usr/bin/python3

import sys
import string
from pathlib import Path


def process_line(text, hist):
    text = text.replace('-', ' ')
    for word in text.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        #Store the word
        hist.add(word)
        
    

def process_file(filename):
    hist = set()

    #Check if file exists and is valid
    filePath = Path(fileName)

    if filePath.exists() and filePath.is_file():

        read_file = open(filename, 'r')
        for line in read_file:
            process_line(line, hist)

    else:
        print(filename + ' is not a vaild file')

    
    return hist

def sorted_freq_list(hist):
    sorted_tuple_list = []
    for key,value in hist.items():
        sorted_tuple_list.append((value,key))

    sorted_tuple_list.sort(reverse=True)

    return sorted_tuple_list

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        fileName2 = sys.argv[2]

        wordsData1 = process_file(fileName)
        wordsData2 = process_file(fileName2)

        diffWords = wordsData1.difference(wordsData2)
        print('Different words which exist in ' + fileName + ' but not in ' + fileName2 + ':')
        print(diffWords)

