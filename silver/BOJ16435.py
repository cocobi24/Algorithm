# https://www.acmicpc.net/problem/16435

n, min = map(int, input().split())
num = sorted(map(int, input().split()))

for n in num :
    if min >= n :
        min += 1
    else :
        break

print(min, end='')