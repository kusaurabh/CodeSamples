#!/usr/bin/python

import sys

file = open('words.txt')
for line in file:
	word = line.strip()
	if len(word) >= 6:
		for i in range(len(word)+1 -6):
			if word[i] == word [i+1] and word[i+2]== word[i+3] and word[i+4] == word[i+5]:
				print(word)



