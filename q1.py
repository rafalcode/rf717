#!/usr/bin/env python3
from random import randint

def foo(length):
    # initialisers
    list = []
    is_done = False
    while (is_done == False):
        r = randint(1,length) # one randnum up and including max val "length"
        is_found = False # set for each randnum
        # first travel through list
        for n in list: 
            if (n==r):
                is_found = True
                # this number is alreayd in in list
                break
        if (is_found == False):
            # this number is not yet in list
            list.append(r)
        if (len(list) == length):
            # list has already reached full complement of possible numbers
            is_done = True
    return list

x = foo(10)
print(x)
