#!/usr/bin/python3

import sys
import string
from pathlib import Path


def process_line(text, hist):
    text = text.replace('-', ' ')
    for word in text.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        #Store the frequency and word
        hist[word] = hist.get(word, 0) + 1
        
    

def process_file(filename):
    hist = dict()

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

        hist = process_file(fileName)

        if len(hist) > 0:
            totalWords = sum(hist.values())
            print('Total Words :' + str(totalWords))
            print('Unique Words:' + str(len(hist)))
            print('Most common words :')
            word_list = sorted_freq_list(hist)
            for freq, word in word_list[0:5]:
                print(word, '\t' , freq)

