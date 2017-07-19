#!/usr/bin/python3

import sys

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i=0
    j=len(word2)-1

    while j >= 0:
        if word1[i] != word2[j]:
            return False

        i = i + 1
        j = j - 1

    return True

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Usage : check_reverse.py <word1> <word2>")
        sys.exit(-1)
    else:
        word1 = sys.argv[1]
        word2 = sys.argv[2]
        result = is_reverse(word1, word2)
        print(result)
    	 
