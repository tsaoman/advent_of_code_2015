# Advent of Code - Day 2 Part 1
# by Brandon Tsao

import sys

ribbon = 0

def facePerimeter(x, y):
    return x + x + y + y

def volume(l, w, h):
    return l * w * h

def minFace(l, w, h):
    return min(facePerimeter(l, w), facePerimeter(w, h), facePerimeter(l, h))

for line in sys.stdin:

    dimensions = line.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    ribbon = ribbon + minFace(l, w, h) + volume(l, w, h)

print ribbon
