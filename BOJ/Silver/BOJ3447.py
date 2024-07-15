# https://www.acmicpc.net/problem/3447

import sys
input = sys.stdin.readline

while True :
    row = input()
    if not row :
        break
    row = row.rstrip().replace("BUG", "")
    while True :
        if "BUG" in row :
            row = row.rstrip().replace("BUG", "")
        else :
            break
    print(row)