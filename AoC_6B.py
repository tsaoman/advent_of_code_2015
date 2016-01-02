#Avent of Code - Day 6 Part 2

import sys

def on(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] += 1

def off(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if lights[x][y] > 0:
                    lights[x][y] -= 1

def toggle(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] += 2

#create 1000 x 1000 grid initialized to False
lights = [[0 for x in range(1000)] for x in range(1000)]

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

print sum(map(sum, lights))
