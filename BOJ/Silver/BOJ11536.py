# https://www.acmicpc.net/problem/11536

n = int(input())
names = [input() for _ in range(n)]
INCREASING = sorted(names)
DECREASING = sorted(names, reverse=True)

if names == INCREASING :
    print("INCREASING")
elif names == DECREASING :
    print("DECREASING")
else :
    print("NEITHER")