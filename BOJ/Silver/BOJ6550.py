# https://www.acmicpc.net/problem/6550

import sys
input = sys.stdin.readline

while True:
    str_list = input().rstrip()
    if not str_list:
        break

    s, t = str_list.split()
    isPartString = False
    idx = 0
    l = len(t)
    for i in range(l):
        if t[i] == s[idx]:
            idx += 1
            if idx == len(s):
                isPartString = True
                break

    print("Yes" if isPartString else "No")