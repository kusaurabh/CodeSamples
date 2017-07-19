#!/usr/bin/python3

import time
import sys
from datetime import timedelta

def prime_list(n):
    """Generates prime numbers till n"""
    if n < 2:
        return []

    size = n//2
    prime_nums = []
    prime_nums.append(2)
    for i in range(1, size):
        val = i*2 + 1
        index = 0;
        for item in prime_nums:
            index+=1
            if val % item == 0:
                break
        if index == len(prime_nums):
            prime_nums.append(val)

    print(prime_nums)
        
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        numLimit = int(sys.argv[1])
        print("Prime numbers till " + str(numLimit))
        starttime = time.time()
        prime_list(numLimit)
        elapsedtime = time.time() - starttime
        print("Computed in " + str(timedelta(elapsedtime)))
    else:
        print("Usage genPrimes <up till number>")
