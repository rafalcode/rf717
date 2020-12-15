#!/usr/bin/env python3
import sys

argquan=len(sys.argv)
if argquan != 2:
    print("rlin: repeat line finder WITHOUT using dictionary nor hash")
    print("      requires one argument, a text file whose lines will be analysed for duplicates")
    sys.exit(2)

# read in the input file in one fell swoop, called a slurp.
with open(sys.argv[1]) as file:
    # lolist, list of lines
    lolines = [line.strip() for line in file]

llen = len(lolines)
for i in range(llen-1):
    # -1 because final line need not be checked against itself.
    for j in range(i+1,llen):
        if(lolines[i] == lolines[j]):
            print(lolines[i])
            # and, because we know it is not unique,
            # we don't bother looking for more repeats.
            break
