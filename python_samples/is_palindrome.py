#!/usr/bin/python3

import sys

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        result = is_palindrome(sys.argv[1])
        print(result)
    else:
        print("Usage : is_palindrome <word>")

