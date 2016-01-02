#Advent of Code - Day 6 Part 1

import sys

def on(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] = True

def off(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] = False

def toggle(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] = not lights[x][y]

#create 1000 x 1000 grid initialized to False
lights = [[False for x in range(1000)] for x in range(1000)]

n = 0 #create a counter for lights that are on

for line in sys.stdin:

    #splits standard input into an array of arguments to be passed to functions
    arguments = line.rstrip().split(' ')

    if arguments[0] == "toggle":
        pair1 = arguments[1].split(',')
        pair2 = arguments[3].split(',')

        toggle(int(pair1[0]), int(pair1[1]), int(pair2[0]), int(pair2[1]))

    elif arguments[0] == "turn":
        pair1 = arguments[2].split(',')
        pair2 = arguments[4].split(',')

        if arguments[1] == "on":
            on(int(pair1[0]), int(pair1[1]), int(pair2[0]), int(pair2[1]))

        elif arguments[1] == "off":
            off(int(pair1[0]), int(pair1[1]), int(pair2[0]), int(pair2[1]))

for i in range(1000):
    for j in range(1000):
        if lights[i][j] == True:
            n += 1

print n
