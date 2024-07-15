# https://www.acmicpc.net/problem/2446

n = int(input())
for i in range(n, 0, -1):
    print(' ' * (n-i), '*' * (n-n+i), '*' * (i-1), sep="")
for i in range(n-1, 0, -1):
    print(' ' * (i-1), '*' * (n-i+1), '*' * (n-i), sep="")