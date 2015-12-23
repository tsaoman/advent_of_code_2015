#Advent of Code - Day 3 Part 1

import sys

houses = [{0: 0}]

X = 0
Y = 0

for char in sys.stdin.read():
    if char == '^':
        Y += 1
    elif char == 'v':
        Y -= 1
    elif char == '>':
        X += 1
    elif char == '<':
        X -= 1

    coordinate = {X: Y}

    if coordinate not in houses:
        houses.append(coordinate)

print len(houses)
