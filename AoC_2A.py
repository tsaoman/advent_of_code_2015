# Advent of Code - Day 2 Part 1
# by Brandon Tsao

import sys

paper = 0

def surfaceArea(l, w, h):
    return (2 * l * w) + (2 * w * h) + (2 * l * h)

def slack(l, w, h):
    return min(l * w, w * h, l * h)

for line in sys.stdin:

    dimensions = line.split('x')

    paper += surfaceArea(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
    paper += slack(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

print paper
