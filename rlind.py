#!/usr/bin/env python3
import sys

argquan=len(sys.argv)
if argquan != 2:
    print("rlind: repeat line finder using a dictionary (which means hash too, because under the hood, that's what dicts are.")
    print("       requires one argument, a text file whose lines will be analysed for duplicates")
    sys.exit(2)

# read in the input file in one fell swoop, called a slurp.
with open(sys.argv[1]) as x: slurpf = x.read()
lin=slurpf.splitlines() # split up into lines,
lasdict= dict() # initialize a Lines as Dictionary dict.
for i in lin:
    # idiom to create a dict key entry when it didn't exist before.
    lasdict[i] = lasdict.get(i, 0) +1

# only print the lines which have been duplicated.
for k in lasdict:
    if(lasdict[k] >1):
        print(k)
