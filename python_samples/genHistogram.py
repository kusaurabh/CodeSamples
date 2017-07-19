#!/usr/bin/python3

def histogram(items):
    items_hist = dict()

    for item in items:
        if item in items_hist:
            prev_count = items_hist[item]
            items_hist[item] = prev_count + 1
        else:
            items_hist[item] = 1

    return items_hist

if __name__ == "__main__":
    word = "Hello"
    hist = histogram(list(word))
    print (hist)
