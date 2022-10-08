# https://www.acmicpc.net/problem/10250

import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split(" "))
    first = n % h
    last = n // h

    if first != 0 and last < 9:
        print(F"{first}0{last + 1}")
    elif first != 0 and last >= 9:
        print(F"{first}{last + 1}")
    elif first == 0 and last <= 9:
        print(F"{h}0{last}")
    else :
        print(F"{h}{last}")