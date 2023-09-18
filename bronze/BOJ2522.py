# https://www.acmicpc.net/problem/2522

n = int(input())
for i in range(n, 0, -1):
    print(' ' * (i-1), '*'*(n+1-i), sep="")
for i in range(1, n):
    print(' ' * i, '*' * (n-i), sep="")