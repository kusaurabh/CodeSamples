#!/usr/bin/python

import sys

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
	number = 35453
	if is_palindrome(str(number)):
		print(number)

