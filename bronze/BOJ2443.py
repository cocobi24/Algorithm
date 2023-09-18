# https://www.acmicpc.net/problem/2443

n = int(input())
for i in range(n, 0, -1):
    print(' ' * (n-i), '*' * (n-n+i), '*' * (i-1), sep="")