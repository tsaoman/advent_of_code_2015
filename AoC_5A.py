#Advent of Code - Day 5 Part 1

import sys
import re

nice = 0

def vowelCheck(string):
    n = 0

    for char in string:
        if char in 'aeiou':
            n += 1

    return n >= 3

def consecutiveCheck(string):
    pattern = re.compile(r'\S*(.)\1\S*')
    return pattern.match(string)

def exclusionCheck(string):
    exclusions = ['ab', 'cd', 'pq', 'xy']

    for word in exclusions:
        if word in string:
            return False

    return True

for line in sys.stdin:
    if (vowelCheck(line) and consecutiveCheck(line) and exclusionCheck(line)):
        nice += 1

print nice
