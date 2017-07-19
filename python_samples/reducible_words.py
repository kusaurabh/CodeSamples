#!/usr/bin/python3

import sys
from datetime import datetime

def check_subwords(word):

    #Exit condition
    if len(word) == 1:
        if word == "a" or word == "i":
            return True
        else:
            return False
    
    #Exit if word is already in reducible words list
    if word in reducible_words:
        return True

    
    status = False
    sub_words = list()
    for pos in range(len(word)):
        sub_word = word[:pos] + word[pos+1:] 
        
        #Check is any of the sub words is legal word and recurse
        if sub_word in word_list:
            check = check_subwords(sub_word)
            status = status or check

    return status


if __name__ == "__main__":

    print(datetime.now())
    
    #Read file with words
    fileHndl = open('words_sample.txt','r')

    global reducible_words
    reducible_words = list()

    global word_list
    word_list = list()
    
    word_list = fileHndl.read().split("\n")
    print(datetime.now())

    for word in word_list:
        #if word is single char and either i or a  add it as reducible
        if len(word) > 1:
            #Identify reducible words
            status =  check_subwords(word)
            if status:
                reducible_words.append(word)
        else:
            if word == "a" or word == "i":
                reducible_words.append(word)
                

    fileHndl.close()
    print(reducible_words)

    print(datetime.now())
