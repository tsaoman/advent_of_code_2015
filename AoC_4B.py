#Advent of Code - Day 4 Part 1

import hashlib

key = "iwrupvqb"
ans = 0

while(1):

    string = key + str(ans)

    if hashlib.md5(string).hexdigest()[0:6] == '000000' :
        print ans
        break

    ans += 1
