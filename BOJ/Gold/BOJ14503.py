# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
block = []
clean = 0

for i in range(N) :
    block.append([])
    row = list(map(int, input().split()))
    for j in range(M) :
        block[i].append(row[j])

def isDirty(block, r, c) :
    if r-1 >= 0 :
        if block[r-1][c] == 0 :
            return True
    if r+1 < N :
        if block[r+1][c] == 0 :
            return True
    if c-1 >= 0 :
        if block[r][c-1] == 0 :
            return True
    if c+1 < M :
        if block[r][c+1] == 0 :
            return True
    return False


while True :
    dirty = 0
    if block[r][c] == 0 :
        block[r][c] = "*"
        clean += 1

    if isDirty(block, r, c) == False :
        if d == 0 :
            if r + 1 < N:
                if block[r+1][c] == 1:
                    break
                else :
                    r += 1
        elif d == 1 :
            if c - 1 >= 0 :
                if block[r][c-1] == 1:
                    break
                else :
                    c -= 1
        elif d == 2 :
            if r - 1 >= 0 :
                if block[r-1][c] == 1:
                    break
                else :
                    r -= 1
        else :
            if c + 1 < M:
                if block[r][c+1] == 1:
                    break
                else :
                    c += 1
    else :
        if d == 0 :
            d = 3
        else :
            d -= 1

        if d == 0 :
            if r - 1 >= 0:
                if block[r-1][c] == 0:
                    r -= 1
        elif d == 1 :
            if c + 1 < M:
                if block[r][c+1] == 0:
                    c += 1
        elif d == 2 :
            if r + 1 < N:
                if block[r+1][c] == 0:
                    r += 1
        else :
            if c - 1 >= 0:
                if block[r][c-1] == 0:
                    c -= 1

print(clean)