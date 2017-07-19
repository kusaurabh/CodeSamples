#!/usr/bin/python3

import sys

def check_duplicates(items):
    list_items = items[:]
    list_items.sort()
    prev_item = None
    for item in list_items:
        if prev_item == item:
            return True
        else:
            prev_item = item
            
    
    return False

def create_unique_list(items):
    unique_list = list()
    for item in items:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

if __name__ == "__main__":
    items = ["Hello", "rt", "st", "lt", "lt"]
    result = check_duplicates(items)
    unqList = create_unique_list(items)
    print(items)
    print(result)
    print(unqList)
