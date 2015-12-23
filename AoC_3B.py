import sys

houses = [{0: 0}]

X = 0
Y = 0

buff = sys.stdin.read()

santa = buff[::2]
robot = buff[1::2]

print santa
print robot

for char in santa:
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

X = 0
Y = 0

for char in robot:
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
