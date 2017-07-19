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

    sorted_tuple_list.sort()

    return sorted_tuple_list

def word_freq_sum(wordFreqList):
    freqSumList = []

    prevCount = 0
    for freq, word in wordFreqList:
        count = prevCount + freq
        freqSumList.append(count)
        prevCount = count

    return freqSumList


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        numWords = 1
        try:
            numWords = int(sys.argv[2])
        except:
            print('Num words arg is invalid genrating 1 word by default')

        hist = process_file(fileName)

        wordList = hist.keys()
        wordFreqList = sorted_freq_list(hist)
        freqSumList = word_freq_sum(wordFreqList)
        
        for freq, word in wordFreqList[0:10]:
            print(word, '\t', freq)        

        print(freqSumList)


