#!/usr/bin/python3

def binary_search(items, valToFind):
    sorted_items = items[:]
    sorted_items.sort()
    start = 0
    end = len(items)-1

    while start <= end:
        mid = (end + start)//2
        if sorted_items[mid] < valToFind:
            start = mid+1
        elif sorted_items[mid] > valToFind:
            end = mid-1
        else:
            return mid

    return -1

if __name__ == "__main__":
    items = [2,3,4,6,5,9,10,11]
    val = 10
    index = binary_search(items,val)
    print(items)
    if index >=0 :
        print(str(val) + " found at " + str(index))
    else:
        print(str(val) + " not found")
    
