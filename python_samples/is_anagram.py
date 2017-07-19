#!/usr/bin/python3

import sys

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    #Compare the chars
    list_char1 = list(word1)
    list_char2 = list(word2)

    for alpha in list_char1:
        if alpha in list_char2:
            continue
        else:
            return False

    return True
 



if __name__ == "__main__":
    if len(sys.argv) == 3:
        result = is_anagram(sys.argv[1], sys.argv[2])
        if result:
            print("YES")
        else:
            print("NO")

    else:
        print("Usage : is_anagram <word1> <word2>")

