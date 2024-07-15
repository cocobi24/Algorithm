# https://www.acmicpc.net/problem/10823

import sys
input = sys.stdin
s = ""
for _ in input :
    s += _.rstrip()
print( sum(list(map(int,s.split(",")))) )